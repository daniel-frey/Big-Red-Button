"""Imports."""
import sys
import os
import pyfiglet
import getpass
import json
import time

# Gloabl Variables
aws_host = 'Input Needed'
security_groups = 'Input Needed'
aws_security_groups = ''
region = 'us-west-2'
output_format = 'JSON'
image_id = 'ami-01e24be29428c15b2'
db_name = 'Input Needed'
db_instance_id = 'Input Needed'
db_storage = 0
db_instance_class = 'db.t2.micro'
db_engine = 'postgres'
db_user_name = 'Input Needed'
db_user_password = 'Input Needed'
key_name = 'Input Needed'


def signage():
    """Create an ascii display based on pyfiglet import."""
    result = pyfiglet.figlet_format("AWS Automator")
    print(result)


def display_menu():
    """."""
    answer = ''
    global aws_host, security_groups, output_format, image_id, db_name, db_instance_id, key_name
    global db_storage, db_instance_class, db_engine, db_user_name, db_user_password, aws_security_groups
    while answer != 'quit' or answer != 'exit' or answer != 'q':
        signage()
        if aws_host == 'Input Needed':
            print(f'1.  EC2: Host Name (used for quick connect to AWS): \033[1;31m { aws_host } \033[0;0m')
        else:
            print(f'1.  EC2: Host Name (used for quick connect to AWS): \033[1;33m { aws_host } \033[0;0m')
        print(f'2.  EC2: Current Region: \033[1;33m { region } \033[0;0m')
        print(f'3.  EC2: Instance to Create: \033[1;33m { image_id } \033[0;0m')
        if security_groups == 'Input Needed':
            print(f'4.  EC2: Current Security Group Name: \033[1;31m { security_groups } \033[0;0m')
        else:
            print(f'4.  EC2: Current Security Group Name: \033[1;33m { security_groups } \033[0;0m')
        print(f'5.  EC2: Current output format: \033[1;33m { output_format } \033[0;0m')
        if db_name == 'Input Needed':
            print(f'6.  RDS: DataBase Name: \033[1;31m { db_name } \033[0;0m')
        else:
            print(f'6.  RDS: DataBase Name: \033[1;33m { db_name } \033[0;0m')
        if db_instance_id == 'Input Needed':
            print(f'7.  RDS: DataBase Instance ID: \033[1;31m { db_instance_id } \033[0;0m')
        else:
            print(f'7.  RDS: DataBase Instance ID: \033[1;33m { db_instance_id } \033[0;0m')
        if db_storage == 0:
            print(f'8.  RDS: DataBase Allocated Storage: \033[1;31m { db_storage } \033[0;0m')
        else:
            print(f'8.  RDS: DataBase Allocated Storage: \033[1;33m { db_storage } \033[0;0m')
        if db_instance_class == 'Input Needed':
            print(f'9.  RDS: DataBase Instance Class: \033[1;31m { db_instance_class } \033[0;0m')
        else:
            print(f'9.  RDS: DataBase Instance Class: \033[1;33m { db_instance_class } \033[0;0m')
        if db_engine == 'Input Needed':
            print(f'10.  RDS: DataBase Engine: \033[1;31m { db_engine } \033[0;0m')
        else:
            print(f'10.  RDS: DataBase Engine: \033[1;33m { db_engine } \033[0;0m')
        if db_user_name == 'Input Needed':
            print(f'11.  RDS: DataBase User Name: \033[1;31m { db_user_name } \033[0;0m')
        else:
            print(f'11.  RDS: DataBase User Name: \033[1;33m { db_user_name } \033[0;0m')
        if db_user_password == 'Input Needed':
            print(f'12.  RDS: DataBase User Password: \033[1;31m { db_user_password } \033[0;0m')
        else:
            print(f'12.  RDS: DataBase User Password: \033[1;33m HIDDEN \033[0;0m')
        if security_groups == 'Input Needed':
            print(f'13.  RDS: DataBase VPC Group: \033[1;31m { security_groups } \033[0;0m')
        else:
            print(f'13.  RDS: DataBase VPC Group: \033[1;33m { security_groups } \033[0;0m')
        if key_name == 'Input Needed':
            print(f'14.  EC2: Key Name: \033[1;31m { key_name } \033[0;0m')
        else:
            print(f'14.  EC2: Key Name: \033[1;33m { key_name } \033[0;0m')

        # print('15.  Display JSON File')

        answer = input('\n(\033[1;31m!\033[0;0m) Execute (\033[1;31mq\033[0;0m) Quit (\033[1;31m?\033[0;0m) Help \
        \nPlease Enter a Selection: ')
        if answer == '?':
            print('\nHELP MENU TO GO HERE\n')
            input('Press ENTER to continue...')

        elif answer == 'q':
            exit()

        elif answer == '1':
            aws_host = input('Enter a file name (press enter to select default ec2_host): ')
            if aws_host is '':
                aws_host = 'ec2_host'

        elif answer == '2':
            print('This option is currently not configurable! Using Option 4. US-WEST-2.')
            print('1. US-EAST-1')
            print('2. US-EAST-2')
            print('3. US-WEST-1')
            print('\033[1;31m4. US-WEST-2\033[0;0m')
            input('Press ENTER to continue...')

        elif answer == '3':
            print('This option is currently not configurable!  Single instance only')
            input('Press ENTER to continue...')

        elif answer == '4':
            security_groups = input('Enter a security group(single word): ')
            if security_groups == '':
                security_groups = 'Input Needed'
            # TODO This will then do a request to amazon to get the Group_ID back from amazon.
            # TODO add error checking to make sure it does not start with SG

        elif answer == '5':
            print('This option is currently not configurable!  JSON Only at this time.')
            input('Press ENTER to continue...')

        elif answer == '6':
            db_name = input('Enter the DataBase Name: ')
            if db_name == '':
                db_name = 'Input Needed'

        elif answer == '7':
            db_instance_id = input('Enter the DataBase Instance ID: ')
            if db_instance_id == '':
                db_instance_id = 'Input Needed'

        elif answer == '8':
            try:
                db_storage = abs(int(float(input('Enter the DataBase Storage (20 to 16384): '))))
                if db_storage == '':
                    db_storage = 0
                    print('Must Enter a Number!')
                    input('Press ENTER to continue...')
                elif db_storage < 20 or db_storage > 16384:
                    db_storage = 0
                    print('Incorrect Range!  Try Again!')
                    input('Press ENTER to continue...')
            except ValueError:
                print('Incorrect Range!  Try Again!')
                input('Press ENTER to continue...')

        elif answer == '9':
            print('This option is currently not configurable!  default free tier.')
            input('Press ENTER to continue...')

        elif answer == '10':
            print('This option is currently not configurable!  Postgres Only.')
            input('Press ENTER to continue...')

        elif answer == '11':
            db_user_name = input('Enter DataBase User Name: ')
            if db_user_name == '':
                db_user_name = 'Input Needed'

        elif answer == '12':
            db_user_password = getpass.getpass('Password: ')

        elif answer == '13':
            vpc_group = input('Enter VPC Group: ')
            if vpc_group == '':
                vpc_group = 'Input Needed'

        elif answer == '14':
            key_name = input('Enter Key Name: ')
            if key_name == '':
                key_name = 'Input Needed'

        # elif answer == '15':
        #     write_json()
        #     print('Still need to display the file')

        elif answer == '!':
            execute_aws()

        else:
            print('\nInvalid!!!!  Please enter a valid option!')
            input('Press ENTER to continue...')


def execute_aws():
    """."""
    print('Generating AWS Security Group ID...')
    get_aws_sg_id()
    time.sleep(4)
    print('Generating JSON file...')
    write_json()
    time.sleep(3)
    print('Initiating EC2 Instance...')
    send_ec2_json_to_aws()
    time.sleep(4)
    print('Initiating RDS Instance...')
    send_rds_json_to_aws()
    time.sleep(4)
    print('EC2 & RDS complete.  Running setup on EC2 Instance.')
    exit()
    print('Initiating RDS Instance...')
    send_rds_json_to_aws
    time.sleep(4)
    print('EC2 & RDS complete.  Running setup on EC2 Instance.')
    exit()



def get_aws_sg_id():
    """."""
    global aws_security_groups
    os.system(f"aws ec2 create-security-group --group-name { security_groups } --description 'Security group for \
    development environment' --output json > sg_id.json")
    sg_aws = open('sg_id.json').read()
    sg_aws_json = json.loads(sg_aws)
    aws_security_groups = sg_aws_json["GroupId"]


def write_json():
    """."""
    global aws_host, security_groups, output_format, image_id, db_name, db_instance_id, key_name
    global db_storage, db_instance_class, db_engine, db_user_name, db_user_password, aws_security_groups
    ec2_data = open('ec2instance_template.json').read()
    ec2_json_data = json.loads(ec2_data)
    ec2_json_data['KeyName'] = key_name
    ec2_json_data['SecurityGroupIds'] = [aws_security_groups]
    ec2_json_data['SecurityGroups'] = [security_groups]
    ec2_json_data['ImageId'] = image_id
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
    rds_json_data['VpcSecurityGroupIds'] = [aws_security_groups]
    with open('rdsinstance_template_completed.json', 'w') as f2:
        json.dump(rds_json_data, f2, sort_keys=False, indent=4)
    return


def send_ec2_json_to_aws():
    """."""
    os.system('aws ec2 run-instances --cli-input-json file://ec2_instance_completed.json')
    return


def send_rds_json_to_aws():
    """."""
    os.system('aws rds create-db-instance --cli-input-json file://rdsinstance_template_completed.json')
    return


def clear_screen():
    """Clears the screen."""
    os.system('clear')
    return


def exit():
    """Function to exit gracefully."""
    sys.exit('\n\nThank you for using the application\n\n')


if __name__ == '__main__':
    try:
        clear_screen()
        display_menu()
    except KeyboardInterrupt:
        print('\n\nThank you for using the application\n\n')
