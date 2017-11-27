# 27 Nov 2017 | TMDb API

import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('nxoracle.py', 'rb')
s3.Bucket('nitinx').put_object(Key='nxoracle.py', Body=data)
