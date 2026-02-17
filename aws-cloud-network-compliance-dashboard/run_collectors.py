###This orchestrates everything
import os
from dotenv import load_dotenv

from collectors import (
    collect_vpcs,
    collect_subnets,
    collect_route_tables,
    collect_security_groups,
    collect_ec2_instances,
)


load_dotenv()

REGION = os.getenv("AWS_REGION")

def main():
    if not REGION:
        raise ValueError("AWS_REGION not set in environment variables")

    print("Collecting AWS resources...")

    collect_vpcs(REGION)
    collect_subnets(REGION)
    collect_route_tables(REGION)
    collect_security_groups(REGION)
    collect_ec2_instances(REGION)

    print("Collection complete.")

