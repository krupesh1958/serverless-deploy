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

    auth_resp = {
        "principalId": "user",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api.invoke",
                    "Effect": effect,
                    "Resource": "arn:aws:execute-api:us-east-1:434634485527:ern6h3gdac/*/*/*"
                }
            ]
        },
        "context": {
            "stringKey": "value",
            "numberKey": "1",
            "booleanKey": "true"
        },
        "usageIdentifierKey": "{api-key}"
    }
    return auth_resp

