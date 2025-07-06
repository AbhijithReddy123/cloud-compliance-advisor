import boto3

def check_ec2_compliance(instances, rules):
    ec2 = boto3.client("ec2", region_name="ap-southeast-2")
    results = []

    allowed_regions = rules.get("allowed_regions", [])
    require_encryption = rules.get("require_encryption", True)

    for instance in instances:
        instance_id = instance["InstanceId"]
        region = instance["Placement"]["AvailabilityZone"][:-1]  # "ap-southeast-2a" → "ap-southeast-2"

        # Get attached volume IDs
        volume_ids = [
            bd["Ebs"]["VolumeId"]
            for bd in instance.get("BlockDeviceMappings", [])
            if "Ebs" in bd
        ]

        # Describe volumes and check encryption
        volumes = ec2.describe_volumes(VolumeIds=volume_ids)["Volumes"]
        encrypted = all(volume.get("Encrypted", False) for volume in volumes)

        # Apply compliance rules from config.yaml
        compliant = (region in allowed_regions) and (encrypted == require_encryption)

        results.append({
            "InstanceId": instance_id,
            "Region": region,
            "Encrypted": encrypted,
            "Compliant": compliant
        })

    return results