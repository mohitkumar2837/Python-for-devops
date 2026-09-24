import boto3
sts = boto3.client("sts")

response = sts.get_caller_identity()

print("AWS Account ID:", response["Account"])
print("User/Role ARN:", response["Arn"])
print("User/Role ID:", response["UserId"])