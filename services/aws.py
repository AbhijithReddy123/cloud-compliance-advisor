import boto3

def get_ec2_instances():
    ec2 = boto3.client("ec2")
    response = ec2.describe_instances()
    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append(instance)

    return instances
