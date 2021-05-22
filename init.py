from boto3.session import Session

access_key= 'AKIAYQ2BVGECQPQVYR7W'
access_secret = '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'

session = Session(aws_access_key_id=access_key,
    aws_secret_access_key=access_secret)

s3 = session.resource('s3')
bucket = "storagebucket5171"
my_bucket = s3.Bucket(bucket)