import boto3
session = boto3.Session(profile_name="managed_snapshots") 
s3 = session.resource('s3')

def list_buckets():
    buckets = []
    buckets = s3.buckets.all()
    return buckets

def create_bucket(bucket_name):
    s3.create_bucket(Bucket=bucket_name)
    #s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={
            'LocationConstraint': 'us-west-1'})

def upload_object(bucket_dest, key_name,file_path)
    s3.Object(bucket_dest,key_name).put(Body=open(file_path,'rb'))

def list_objcets(bucket_name):
    for bucket in buckets:
        for key in bucket.objects.all():
            print(key.key)

def delete_bucket(bucket_name):
    bucket = s3.Bucket(bucket_name)
    for key in bucket.objects.all():
        key.delete()
    bucket.delete()






def main():
    buckets = list_buckets()
    for b in buckets:
        print(b)

if __name__ == '__main__':
    main()
