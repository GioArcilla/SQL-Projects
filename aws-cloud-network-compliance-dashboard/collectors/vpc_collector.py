import boto3
from db.database import engine

def collect_vpcs(region):
    ec2 = boto3.client("ec2", region_name=region)
    response = ec2.describe_vpcs()

    with engine.connect() as conn:
        for vpc in response["Vpcs"]:
            conn.execute(
                """
                INSERT INTO vpcs (vpc_id, cidr_block, is_default, state)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (vpc_id) DO NOTHING;
                """,
                (
                    vpc["VpcId"],
                    vpc["CidrBlock"],
                    vpc.get("IsDefault", False),
                    vpc["State"]
                )
            )
