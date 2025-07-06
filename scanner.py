import boto3

def check_public_s3():
    s3 = boto3.client('s3')
    public_buckets = []

    for bucket in s3.list_buckets()['Buckets']:
        name = bucket['Name']
        acl = s3.get_bucket_acl(Bucket=name)
        for grant in acl['Grants']:
            grantee = grant.get('Grantee', {})
            if grantee.get('URI') == 'http://acs.amazonaws.com/groups/global/AllUsers':
                public_buckets.append(name)

    return public_buckets


def run_compliance_checks():
    issues = []

    publics = check_public_s3()
    if publics:
        issues.append({
            "type": "S3 Public Access",
            "severity": "High",
            "resources": publics,
            "remediation": "Restrict access using bucket policies or ACLs. Disable public access settings in S3."
        })

    return issues