import json

ec2_data = open('ec2instance_template.json').read()
ec2_json_data = json.loads(ec2_data)

print(ec2_json_data)

ec2_json_data["NetworkInterfaces"][0]["Ipv6Addresses"][0]["Ipv6Address"] = ipv6_address
ec2_json_data['KeyName'] = key_name
ec2_json_data['SecurityGroupIds'] = []
ec2_json_data['SecurityGroups'] = security_groups
ec2_json_data['ImageId'] = image_id
ec2_json_data['Placement'][0]["AvailabilityZone"] = region

print(ec2_json_data)

with open('ec2_instance_completed.json', 'w') as f:
    json.dump(ec2_json_data, f, sort_keys=False, indent=4)


rds_data = open('rdsinstance_template.json').read()
rds_json_data = json.loads(rds_data)

rds_json_data['DBName'] = db_name
rds_json_data['DBInstanceIdentifier'] = db_instance_id
rds_json_data['AllocatedStorage'] = db_storage
rds_json_data['DBInstanceClass'] = db_instance_class
rds_json_data['Engine'] = db_engine
rds_json_data['MasterUsername'] = db_user_name
rds_json_data['MasterUserPassword'] = db_user_password
rds_json_data['VpcSecurityGroupIds'] = vpc_group

with open('rdsinstance_template_completed.json', 'w') as f2:
    json.dump(rds_json_data, f2, sort_keys=False, indent=4)
