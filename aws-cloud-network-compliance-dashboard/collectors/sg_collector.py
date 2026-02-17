import boto3
from db.database import engine


def collect_security_groups(region):
    ec2 = boto3.client("ec2", region_name=region)
    response = ec2.describe_security_groups()

    with engine.begin() as conn:
        for sg in response["SecurityGroups"]:
            sg_id = sg["GroupId"]
            vpc_id = sg["VpcId"]
            name = sg.get("GroupName")
            description = sg.get("Description")

            # Insert security group
            conn.execute(
                """
                INSERT INTO security_groups (sg_id, vpc_id, name, description)
                VALUES (
                    %s,
                    (SELECT id FROM vpcs WHERE vpc_id = %s),
                    %s,
                    %s
                )
                ON CONFLICT (sg_id) DO NOTHING;
                """,
                (sg_id, vpc_id, name, description),
            )

            # Ingress rules
            for permission in sg.get("IpPermissions", []):
                protocol = permission.get("IpProtocol")
                from_port = permission.get("FromPort")
                to_port = permission.get("ToPort")

                for ip_range in permission.get("IpRanges", []):
                    cidr = ip_range.get("CidrIp")

                    conn.execute(
                        """
                        INSERT INTO security_group_rules
                        (sg_id, protocol, from_port, to_port, cidr_block, direction)
                        VALUES (
                            (SELECT id FROM security_groups WHERE sg_id = %s),
                            %s, %s, %s, %s, 'ingress'
                        )
                        ON CONFLICT DO NOTHING;
                        """,
                        (sg_id, protocol, from_port, to_port, cidr),
                    )

            # Egress rules
            for permission in sg.get("IpPermissionsEgress", []):
                protocol = permission.get("IpProtocol")
                from_port = permission.get("FromPort")
                to_port = permission.get("ToPort")

                for ip_range in permission.get("IpRanges", []):
                    cidr = ip_range.get("CidrIp")

                    conn.execute(
                        """
                        INSERT INTO security_group_rules
                        (sg_id, protocol, from_port, to_port, cidr_block, direction)
                        VALUES (
                            (SELECT id FROM security_groups WHERE sg_id = %s),
                            %s, %s, %s, %s, 'egress'
                        )
                        ON CONFLICT DO NOTHING;
                        """,
                        (sg_id, protocol, from_port, to_port, cidr),
                    )
