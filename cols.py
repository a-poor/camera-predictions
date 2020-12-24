
import pandas as pd

df = pd.read_csv(
    "data/photos.tsv000",
    sep="\t"
)[[
    "photo_id",
    "photo_image_url",
    "photo_width",
    "photo_height",
    "photo_aspect_ratio",
    "exif_camera_make",
    "exif_camera_model",
    "exif_iso",
    "exif_aperture_value",
    "exif_focal_length",
    "exif_exposure_time",
]].dropna()




