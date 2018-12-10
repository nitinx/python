# 09 Nov 2017 | AWS Integration

import boto3

# Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
#data = open('nxoracle.py', 'rb')
#s3.Bucket('nitinx').put_object(Key='nxoracle.py', Body=data)

# Amazon EC2
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)
