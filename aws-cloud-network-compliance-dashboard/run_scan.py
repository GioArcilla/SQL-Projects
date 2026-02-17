###Orchestrates compliance checks and stores findings
from compliance.checks import check_open_security_groups
from db.database import engine

def insert_findings(findings):
    with engine.connect() as conn:
        for f in findings:
            conn.execute(
                """
                INSERT INTO compliance_findings
                (resource_type, resource_id, severity, description)
                VALUES (%s, %s, %s, %s);
                """,
                (
                    f["resource_type"],
                    f["resource_id"],
                    f["severity"],
                    f["description"]
                )
            )

def main():
    print("Running compliance scan...")

    findings = []
    findings += check_open_security_groups()

    insert_findings(findings)

    print(f"Total findings: {len(findings)}")

if __name__ == "__main__":
    main()
