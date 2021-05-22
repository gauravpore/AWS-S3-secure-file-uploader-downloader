from init import my_bucket

def delete(key):
    my_bucket.delete_objects(Delete={'Objects':[{"Key":key}]})
