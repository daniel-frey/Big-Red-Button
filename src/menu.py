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
db_storage = 20
db_instance_class = 'db.t2.micro'
db_engine = 'postgres'
db_user_name = 'Input Needed'
db_user_password = 'Input Needed'
key_name = 'Input Needed'
ready_to_go = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]


def signage():
    """Create an ascii display based on pyfiglet import.
    Variable result will set what to display on the screen.
    """

    result = pyfiglet.figlet_format("AWS Automator")
    print(result)


def display_menu():
    """."""
    answer = ''
    global aws_host, security_groups, output_format, image_id, db_name, db_instance_id, key_name, ready_to_go
    global db_storage, db_instance_class, db_engine, db_user_name, db_user_password, aws_security_groups, region
    while answer != 'quit' or answer != 'exit' or answer != 'q':
        signage()

        if aws_host == 'Input Needed':
            print(f'1.  EC2: Host Name (used for quick connect to AWS): \033[1;31m { aws_host } \033[0;0m')
            ready_to_go[0] = False
        else:
            print(f'1.  EC2: Host Name (used for quick connect to AWS): \033[1;33m { aws_host } \033[0;0m')
            ready_to_go[0] = True

        print(f'2.  EC2: Current Region: \033[1;33m { region } \033[0;0m')
        ready_to_go[1] = True

        print(f'3.  EC2: Instance to Create: \033[1;33m { image_id } \033[0;0m')
        ready_to_go[2] = True

        if security_groups == 'Input Needed':
            print(f'4.  EC2: Current Security Group Name: \033[1;31m { security_groups } \033[0;0m')
            ready_to_go[3] = False
        else:
            print(f'4.  EC2: Current Security Group Name: \033[1;33m { security_groups } \033[0;0m')
            ready_to_go[3] = True

        print(f'5.  EC2: Current output format: \033[1;33m { output_format } \033[0;0m')
        ready_to_go[4] = True

        if db_name == 'Input Needed':
            print(f'6.  RDS: DataBase Name: \033[1;31m { db_name } \033[0;0m')
            ready_to_go[5] = False
        else:
            print(f'6.  RDS: DataBase Name: \033[1;33m { db_name } \033[0;0m')
            ready_to_go[5] = True

        if db_instance_id == 'Input Needed':
            print(f'7.  RDS: DataBase Instance ID: \033[1;31m { db_instance_id } \033[0;0m')
            ready_to_go[6] = False
        else:
            print(f'7.  RDS: DataBase Instance ID: \033[1;33m { db_instance_id } \033[0;0m')
            ready_to_go[6] = True

        if db_storage == 0:
            print(f'8.  RDS: DataBase Allocated Storage: \033[1;31m { db_storage } \033[0;0m')
            ready_to_go[7] = False
        else:
            print(f'8.  RDS: DataBase Allocated Storage: \033[1;33m { db_storage } \033[0;0m')
            ready_to_go[7] = True

        if db_instance_class == 'Input Needed':
            print(f'9.  RDS: DataBase Instance Class: \033[1;31m { db_instance_class } \033[0;0m')
            ready_to_go[8] = False
        else:
            print(f'9.  RDS: DataBase Instance Class: \033[1;33m { db_instance_class } \033[0;0m')
            ready_to_go[8] = True

        if db_engine == 'Input Needed':
            print(f'10.  RDS: DataBase Engine: \033[1;31m { db_engine } \033[0;0m')
            ready_to_go[9] = False
        else:
            print(f'10.  RDS: DataBase Engine: \033[1;33m { db_engine } \033[0;0m')
            ready_to_go[9] = True

        if db_user_name == 'Input Needed':
            print(f'11.  RDS: DataBase User Name: \033[1;31m { db_user_name } \033[0;0m')
            ready_to_go[10] = False
        else:
            print(f'11.  RDS: DataBase User Name: \033[1;33m { db_user_name } \033[0;0m')
            ready_to_go[10] = True

        if db_user_password == 'Input Needed':
            print(f'12.  RDS: DataBase User Password: \033[1;31m { db_user_password } \033[0;0m')
            ready_to_go[11] = False
        else:
            print(f'12.  RDS: DataBase User Password: \033[1;33m HIDDEN \033[0;0m')
            ready_to_go[11] = True

        if security_groups == 'Input Needed':
            print(f'13.  RDS: DataBase VPC Group: \033[1;31m { security_groups } \033[0;0m')
            ready_to_go[12] = False
        else:
            print(f'13.  RDS: DataBase VPC Group: \033[1;33m { security_groups } \033[0;0m')
            ready_to_go[12] = True

        if key_name == 'Input Needed':
            print(f'14.  EC2: Key Name: \033[1;31m { key_name } \033[0;0m')
            ready_to_go[13] = False
        else:
            print(f'14.  EC2: Key Name: \033[1;33m { key_name } \033[0;0m')
            ready_to_go[13] = True

        answer = input('\n(\033[1;31m!\033[0;0m) Execute (\033[1;31mq\033[0;0m) Quit (\033[1;31m?\033[0;0m) Help \
        \nPlease Enter a Selection: ')
        if answer == '?':
            print('1. EC2 Host Name - Single Word.  Used to connect via SSH to the EC2 instance as such: ssh ec2_host')
            print('2. Region - Menu selection:  Determines which region servers are used for instance.')
            print('3. EC2 Instance - Specific to each region and they type of server to create.')
            print('4. EC2 Security Group - Security Group will be created in EC2 for access to instance')
            print('5. EC2 Output Format - pre-configured to JSON')
            print('6. RDS DataBase Name - Name of Database.  Single word, no special characters')
            print('7. RDS DataBase Instance - ')
            print('8. RDS DataBase Storage - Storage from 20 GB to 16,384 GB')
            print('9. RDS Instance Class - pre-configured to db.t2.micro')
            print('10. RDS DataBase Engine - pre-configured for postgres')
            print('11. RDS User Name - This will create the user name for your DataBase')
            print('12. RDS User Password - This will create the password for your DataBase')
            print('13. RDS - Will be the same as security group to link the instances')
            print('14. EC2 Key Name - This must match Key created on AWS')
            print('!   Generates EC2 and RDS based on user provided data.')

            input('Press ENTER to continue...')

        elif answer == 'q':
            exit()

        elif answer == '1':
            aws_host = input('Enter a file name (press enter to select default ec2_host): ')
            if aws_host is '':
                aws_host = 'ec2_host'
                ready_to_go[0] = False
            ready_to_go[0]

        elif answer == '2':
            print('This option is not configurable at this time')
            print('1. US-EAST-1')
            print('2. US-EAST-2')
            print('3. US-WEST-1')
            print('\033[1;31m4. US-WEST-2\033[0;0m')
            input('Press ENTER to continue...')

        elif answer == '3':
            print('This option is not configurable at this time! ')
            input('Press ENTER to continue...')

        elif answer == '4':
            security_groups = input('Enter a security group (single word): ')
            if security_groups == '':
                security_groups = 'Input Needed'

        elif answer == '5':
            print('This option is not configurable at this time! ')
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
                if db_storage < 20 or db_storage > 16384:
                    db_storage = 20
                    print('Incorrect Range!  Try Again!')
                    input('Press ENTER to continue...')
            except ValueError:
                print('Incorrect Range!  Try Again!')
                input('Press ENTER to continue...')

        elif answer == '9':
            print('This option is not configurable at this time! ')
            input('Press ENTER to continue...')

        elif answer == '10':
            print('This option is not configurable at this time!')
            input('Press ENTER to continue...')

        elif answer == '11':
            db_user_name = input('Enter DataBase User Name: ')
            if db_user_name == '':
                db_user_name = 'Input Needed'

        elif answer == '12':
            user_passwords()

        elif answer == '13':
            vpc_group = input('Enter VPC Group: ')
            if vpc_group == '':
                vpc_group = 'Input Needed'

        elif answer == '14':
            key_name = input('Enter Key Name: ')
            if key_name == '':
                key_name = 'Input Needed'

        elif answer == '15':
            aws_host = 'test_host'
            security_groups = 'test_security'
            aws_security_groups = 'test'
            region = 'us-west-2'
            output_format = 'JSON'
            image_id = 'ami-01e24be29428c15b2'
            db_name = 'test_database'
            db_instance_id = 'test_db_inst'
            db_storage = 20
            db_instance_class = 'db.t2.micro'
            db_engine = 'postgres'
            db_user_name = 'tester'
            db_user_password = 'password'
            key_name = 'test_key'

        elif answer == '!':
            if False in ready_to_go:
                print(ready_to_go)
                print('Provide ALL required input')
                input('Press ENTER to continue...')
            else:
                print(ready_to_go)
                execute_aws()
                exit()

        else:
            print('\nInvalid!!!!  Please enter a valid option!')
            input('Press ENTER to continue...')


def execute_aws():
    """Calls to functions to generate SG, EC2, and RDS."""
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
    print('Initiating RDS Instance...')
    send_rds_json_to_aws
    time.sleep(4)
    print('EC2 & RDS complete.  Running setup on EC2 Instance.')
    exit()


def get_aws_sg_id():
    """This fucnton makes a seperate call to AWS to create security group."""
    global aws_security_groups
    os.system(f"aws ec2 create-security-group --group-name { security_groups } --description 'Security group for \
    development environment' --output json > sg_id.json")
    sg_aws = open('sg_id.json').read()
    sg_aws_json = json.loads(sg_aws)
    aws_security_groups = sg_aws_json["GroupId"]


def write_json():
    """Function that writes menu data to the JSON file."""
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


def user_passwords():
    """Function that will prompt user for password and validate password."""
    global ready_to_go, db_user_password
    db_user_password = getpass.getpass('Password: ')
    db_user_password1 = getpass.getpass('Enter again for verification: ')
    if db_user_password != db_user_password1:
        print('Password do not match.  Try Again.')
        input('Press ENTER to continue...')
        if ready_to_go is not False:
            ready_to_go = False
        user_passwords()
    db_user_password1 = ''
    return


def send_ec2_json_to_aws():
    """Command to create the EC2 instance with menu data."""
    os.system('aws ec2 run-instances --cli-input-json file://ec2_instance_completed.json')
    return


def send_rds_json_to_aws():
    """Command to create the RDS instance with menu data."""
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
