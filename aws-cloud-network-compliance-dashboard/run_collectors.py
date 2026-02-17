###This orchestrates everything
import os
from dotenv import load_dotenv

from collectors.vpc_collector import collect_vpcs
from collectors.subnet_collector import collect_subnets

load_dotenv()

REGION = os.getenv("AWS_REGION")

def main():
    print("Collecting AWS resources...")
    collect_vpcs(REGION)
    collect_subnets(REGION)
    print("Collection complete.")

if __name__ == "__main__":
    main()
