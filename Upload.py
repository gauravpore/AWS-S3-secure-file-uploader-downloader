from init import my_bucket

def upload(fileName, objName):
   my_bucket.upload_file(fileName, objName)