"""
Lambda handalar to authenticate the functions
"""
from __future__ import annotations

import json


def lambda_handler(event, context):
    """
    This function has to created for only authentication purpose.
    """
    auth = event["Authentication"]

    effect = "Deny"
    if auth == "allow":
        effect = "Allow"
    
    auth_resp = generate_policy(
        principal_id="user",
        effect=effect,
        resource=event["methodArn"]
    )
    return auth_resp


def generate_policy(
    principal_id: str,
    effect: str,
    resource: str
) -> json:
    """
    `Is authentication token is valid then how to pass message to api-gateway to 
    understand that hey, this token is valid please go future process.`
    This function has solved this questions.
    """
    auth_resp = {
        "principal_Id": principal_id
    }
    if effect and resource:
        policy = {
            "Version": "2012-10-17",
            "Statement": []
        }
        statement = {
            "Action": "execute-api:Invoke",
            "Effect": effect,
            "Resource": resource
        }
        policy["Statement"] = [statement]
        auth_resp["policyDocument"] = policy
    
    auth_resp["context"] = {
        "stringKey": "stringval",
        "numberKey": 123,
        "booleanKey": True
    }
    return json.dumps(auth_resp)
