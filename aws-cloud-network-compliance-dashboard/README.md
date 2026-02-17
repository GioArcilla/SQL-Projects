# AWS Cloud Network Compliance & Visibility Dashboard

## Overview
Automated AWS network auditing tool that collects VPC, subnet,
security group, and EC2 data into PostgreSQL (RDS) and performs
compliance scans for security misconfigurations.

## Tech Stack
- Python
- boto3
- PostgreSQL (AWS RDS)
- SQLAlchemy
- Flask

## Architecture
See architecture.png

## Setup
1. Configure AWS profile/credentials
2. Configure .env
3. Run schema.sql
4. python run_collectors.py
5. python run_scan.py
6. python api/app.py

## Output Example
- Security group open to 0.0.0.0/0
- Public EC2 with public IP
- Default VPC detected

### Version History:
2-16-2026: Initial repo and deployment 
2-16=2026: Initial environment deployed
