import os
import requests
import shutil
from download_util import download_file

THIS_FILE_PATH = os.path.abspath(__file__)
#print(THIS_FILE_PATH)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
#print(BASE_DIR)
DOWNLOADS_DIR = os.path.join(BASE_DIR, 'downloads')
#print(DOWNLOADS_DIR)
os.makedirs(DOWNLOADS_DIR, exist_ok=True)


downloaded_img_path = os.path.join(DOWNLOADS_DIR, '1.jpg')
url = 'https://upload.travelawaits.com/ta/uploads/2021/06/shutterstock_1533304598-800x750.jpg'

# a smaller item
r = requests.get(url, stream=True)
r.raise_for_status()
with open (downloaded_img_path, 'wb') as f:
    f.write(r.content)


# larger files
# dl_filename = os.path.basename(url)
# new_dl_path = os.path.join(DOWNLOADS_DIR, dl_filename)


# with requests.get(url, stream=True) as r:
#     with open (new_dl_path, 'wb') as file_obj:
#         shutil.copyfileobj(r.raw, file_obj)


download_file(url, DOWNLOADS_DIR)