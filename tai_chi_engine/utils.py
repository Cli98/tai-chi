from tai_chi_tuna.utils import clean_name
from pathlib import Path
import os
import pandas as pd
import glob

def df_creator_image_folder(path: Path) -> pd.DataFrame:
    """
    Create a dataframe ,
    Which list all the image path under a system folder
    """
    path = Path(path)
    files = []
    formats = ["jpg", "jpeg", "png"]
    for fmt in formats:
        files.extend(path.rglob(f"*.{fmt.lower()}"))
        files.extend(path.rglob(f"*.{fmt.upper()}"))
    return pd.DataFrame({"path": files}).sample(frac=1.).reset_index(drop=True)


def df_creator_auto_folder(dataset_dir):
    image_dir = os.path.join(dataset_dir, 'image_2')
    lidar_dir = os.path.join(dataset_dir, 'velodyne')
    calib_dir = os.path.join(dataset_dir,  'calib')
    label_dir = os.path.join(dataset_dir,  'label_2')

    sample_id_list = [0,1,2]
    imgs = glob.glob(os.path.join(image_dir, "*.png"))
    record = []
    for i in range(len(sample_id_list)):
        dic = {}
        file_prefix = imgs[i].split("/")[-1]
        lidar_path = os.path.join(lidar_dir, file_prefix.replace("png", "bin"))
        calib_path = os.path.join(calib_dir, file_prefix.replace("png", "txt"))
        label_path = os.path.join(label_dir, file_prefix.replace("png", "txt"))
        dic['image_path'] = imgs[i]
        dic['lidar_path'] = lidar_path
        dic['calib_path'] = calib_path
        dic['label_path'] = label_path
        record.append(dic)
    record = pd.DataFrame(record).reset_index(drop=True)
    return record