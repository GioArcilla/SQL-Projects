# Compliance Dashboard
This dashboard will pull AWS networking resources
- VPCs
- Subnets
- Route Tables
- Internet Gateways
- NAT Gateways
- Security Groups
- EC2 instances
- Elastic IPs

## Values
will then be stored relationally in PostgreSQL (RDS)

## Run compliance checks:
- Open security groups (0.0.0.0/0)
- Public subnets with NACL restrictions
- Unattached EBS volumes
- Unused Elastic IPs
- Instances without tags
- Subnets without route to IGW
- Overlapping CIDR ranges
- Default VPC usage detection

## Output:
1) CLI report
2) JSON output
3) Optional Flask API endpoint

### Version History:
2-16-2026: Initial repo and deployment 

