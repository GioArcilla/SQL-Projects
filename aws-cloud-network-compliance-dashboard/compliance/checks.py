###compliance logic stored here
from db.database import engine

def check_open_security_groups():
    query = """
        SELECT sg_id, cidr_block
        FROM security_group_rules
        WHERE cidr_block = '0.0.0.0/0'
        AND direction = 'ingress';
    """

    findings = []

    with engine.connect() as conn:
        result = conn.execute(query)
        for row in result:
            findings.append({
                "resource_type": "security_group",
                "resource_id": row[0],
                "severity": "CRITICAL",
                "description": "Security group open to 0.0.0.0/0"
            })

    return findings

###Any additional checks in this file only
