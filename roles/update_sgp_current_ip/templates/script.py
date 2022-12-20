import boto3

import requests
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
my_ip = ""

def myip():
    global my_ip
    url = "http://checkip.amazonaws.com/"
    ip_response = requests.request("GET", url)
    my_ip = (ip_response.text)
    my_ip = my_ip.replace("\n", "")
    return my_ip

def modify_sgp():
    ip = myip()
    sg_rules_list = [
        {
            'SecurityGroupRuleId':'sgr-09409123fa952c7df' ,
            'SecurityGroupRule': {
                'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'CidrIpv4': f"{ip}/32",
                'Description': 'Added SSH port via script'
            }
        }
    ]
    try:
        response = ec2.modify_security_group_rules(GroupId='sg-0aa713ae41d6e936b', SecurityGroupRules=sg_rules_list)
        print(f"Response code = {response['ResponseMetadata']['HTTPStatusCode']}")
    except ClientError as e:
        print(e)

modify_sgp()