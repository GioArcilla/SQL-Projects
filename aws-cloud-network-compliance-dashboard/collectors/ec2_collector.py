import boto3
from db.database import engine


def collect_ec2_instances(region):
    ec2 = boto3.client("ec2", region_name=region)
    response = ec2.describe_instances()

    with engine.begin() as conn:
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instance_id = instance["InstanceId"]
                subnet_id = instance.get("SubnetId")
                private_ip = instance.get("PrivateIpAddress")
                public_ip = instance.get("PublicIpAddress")
                state = instance.get("State", {}).get("Name")
                has_public_ip = public_ip is not None

                conn.execute(
                    """
                    INSERT INTO ec2_instances
                    (instance_id, subnet_id, private_ip, public_ip, state, has_public_ip)
                    VALUES (
                        %s,
                        (SELECT id FROM subnets WHERE subnet_id = %s),
                        %s, %s, %s, %s
                    )
                    ON CONFLICT (instance_id) DO NOTHING;
                    """,
                    (
                        instance_id,
                        subnet_id,
                        private_ip,
                        public_ip,
                        state,
                        has_public_ip,
                    ),
                )
