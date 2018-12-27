 aws ec2 create-security-group --group-name testgroup --description "Security group for development environment"

	<<  sg-02cdf120e02b4ac20  >>

aws ec2 authorize-security-group-ingress --group-name testgroup --protocol tcp --port 22 --cidr 0.0.0.0/0


aws ec2 create-key-pair --key-name testgroup-key --query "KeyMaterial" --output text > testgroup-key.pem

chmod 400 testgroup-key.pem

aws ec2 run-instances --image-id ami-0bbe6b35405ecebdb --security-group-ids sg-02cdf120e02b4ac20 --count 1 --instance-type t2.micro --key-name testgroup-key --query "Instances[0].InstanceId"

	<<  i-0dfb108cce1a0180a  >>

aws ec2 describe-instances --instance-ids i-0dfb108cce1a0180a --query "Reservations[0].Instances[0].PublicIpAddress"

	<<  54.184.253.242  >>

ssh -i testgroup-key.pem ubuntu@54.184.253.242



aws  create-db-instance--db-instance-identifier testgroup --engine postgres



aws rds create-db-instance --allocated-storage 20 --db-instance-class db.t2.micro --db-instance-identifier test-instance --engine postgres --master-username master --master-user-password secret99


aws describe-instances
