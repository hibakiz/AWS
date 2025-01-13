import boto3
# change the region name below 
region = 'me-south-1'
#change the Instance ID 
instances = ['i-xxxxxxxxxxx',]
ec2 = boto3.client('ec2', region_name=region)
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)