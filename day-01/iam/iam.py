import boto3

iam = boto3.client("iam")

# response = iam.list ()

# for role in response["Roles"]:
#     print(role["RoleName"])


paginator = iam.get_paginator("list_users")

for page in paginator.paginate():
    for user in page["Users"]:
        print("Username:", user["UserName"])
        print("ARN:", user["Arn"])
        print("Created:", user["CreateDate"])
        print("-" * 50)