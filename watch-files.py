import time, boto3
from datetime import datetime

s3 = boto3.resource("s3")
bucket = s3.Bucket("ap-unsplash-images")
total = 21_182

while True:
    count = sum(1 for _ in bucket.objects.all())
    print(f"[{datetime.now()}] {count/total*100:6.2f} % IMAGES PROCESSED")
    time.sleep(60*5)
    
    