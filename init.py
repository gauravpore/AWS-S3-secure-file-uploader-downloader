from boto3.session import Session

access_key= 'Enter access key here'
access_secret = 'Enter secret here'

session = Session(aws_access_key_id=access_key,
    aws_secret_access_key=access_secret)

s3 = session.resource('s3')
bucket = "storagebucket5171"
my_bucket = s3.Bucket(bucket)
