import io
import boto3
import numpy as np
import pandas as pd
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms


class FoculLengthDataset(Dataset):
    def __init__(self, df):
        # Connect to S3
        s3 = boto3.resource("s3")
        self.s3_bucket = s3.Bucket("ap-unsplash-images")
        # Store the DataFrame
        self.df = df.reset_index(drop=True)[["s3_key","exif_focal_length"]]
        # Build transforms
        self.transforms = transforms.Compose([
            transforms.Resize((512,512)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.56040615,0.36607313,0.42010993],
                std=[0.2895784,0.23586935,0.22863376]
            )
        ])
    
    def __len__(self):
        return len(self.df)
    
    def __getitem__(self,i):
        label = self.df.loc[i,"exif_focal_length"]
        s3key = self.df.loc[i,"s3_key"]
        with io.BytesIO() as b:
            self.s3_bucket.download_fileobj(s3key,b)
            b.seek(0)
            tens = self.transforms(Image.open(b))
        return label, tens
        
        