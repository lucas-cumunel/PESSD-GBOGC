import gdown
import zipfile
import os

#download url
url = "https://drive.google.com/drive/folders/1clvz-pXZgjGlvoKWVnHNH96iC1yDUvtc?usp=sharing"
gdown.download_folder(url, quiet=False)


#Unzipping
folder_path = "./PESSD"

for file in os.listdir(folder_path):
    if file.endswith(".zip"):
        zip_path = os.path.join(folder_path, file)
        extract_path = os.path.join(folder_path, file.replace(".zip", ""))

        print(f"Unzipping: {file} → {extract_path}")

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
