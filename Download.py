from init import my_bucket

def download(objName,path):
    my_bucket.download_file(objName,path)