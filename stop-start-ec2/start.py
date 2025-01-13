import boto3
# change the region name below 
region = 'me-south-1'
#change the Instance ID 
instances = ['i-xxxxxxxx',]
ec2 = boto3.client('ec2', region_name=region)
def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)