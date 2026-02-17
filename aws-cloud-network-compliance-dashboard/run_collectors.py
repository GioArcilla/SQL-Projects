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
    print("Collecting AWS resources...")
    collect_vpcs(REGION)
    collect_subnets(REGION)
    print("Collection complete.")

if __name__ == "__main__":
    main()
