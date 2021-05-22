# AWS-S3-file-Uploader-Downloader
## Overview:
[Amazon S3](https://aws.amazon.com/s3/) is a service offered by [AWS](https://aws.amazon.com/) which has a simple web services interface that you can use to store and retrieve any amount of data, at any time, from anywhere on the web. It gives any developer access to the same highly scalable, reliable, fast, inexpensive data storage infrastructure that Amazon uses to run its own global network of web sites.
The objective is to create secure file controller to upload, download and delete files to and from [Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html) using Python scripts to enable automation and flexibility.

### Concepts:
- Cloud Computing
- AWS Fundamentals

### Tools & Technologies:
- [AWS Management Console](https://aws.amazon.com/console/)
- Amazon Simple Storage Service ([Amazon S3](https://aws.amazon.com/s3/))
- Python
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/session.html)

> Installation Guide:
```
pip install boto3
```
### Implementation:
- Step 1: Setup your Amazon S3 service and create a Bucket using [AWS management console](https://aws.amazon.com/console/)

***NOTE:***
To get started with AWS and to create Amazon S3 Bucket, go through this [Quick Start Guide](https://docs.aws.amazon.com/quickstarts/latest/s3backup/welcome.html).

- Step 2:  Get `access key`,`access secret` & bucket name, in order to initiate the session.
- Step 3: Run [```Test.py```](https://github.com/gauravpore/AWS-S3-file-Uploader-Downloader/blob/main/Test.py) and select the desired operation to be performed. 

## References:
[AWS Quick Starts](https://docs.aws.amazon.com/index.html)

## Contribution:
Contributions are always welcomed. Make sure you read the [Contribution info](https://github.com/gauravpore/AWS-S3-file-Uploader-Downloader/blob/main/contribution.md) before making pull request.

## Screenshots:
#### Console:
![alt tag](https://user-images.githubusercontent.com/67472558/119215891-1dceb180-baee-11eb-896a-695ab66c9f26.JPG "AWS management console")

#### Test run:
![alt tag](https://user-images.githubusercontent.com/67472558/119215892-1f987500-baee-11eb-9dfd-612933c1e60d.JPG "Test run")

