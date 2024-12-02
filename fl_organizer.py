import os
import shutil
from datetime import datetime

source = input("Directory Absolute Path: ").replace("\\", "/").replace("\"", "", 2).replace("\'", "", 2)

if not os.path.exists(source):
    print(f"The folder '{source}' does not exist.")
    exit()
if len(os.listdir(source)) == 0:
    print(f"There are no .flp file in {source}")
    exit()
for file in os.listdir(source):
    is_flp_file = file[-1]==("p") and file[-2]==("l") and file[-3]==("f") and file[-4]==(".")
    if is_flp_file:
        if source[-1]=="/":
            file_path = source + file
        else:
            file_path = source + "/" + file
                

        creation_year = datetime.fromtimestamp(os.path.getctime(file_path)).year

        year_folder = os.path.join(source, str(creation_year))
        if not os.path.exists(year_folder):
            os.makedirs(year_folder)
        
        new_folder_path = os.path.join(year_folder, file[:-4])
        
        os.makedirs(new_folder_path, exist_ok=True)

        shutil.move(file_path, os.path.join(new_folder_path, file))
        if os.path.exists(file_path[:-4]+".mp3"):
            shutil.move(file_path[:-4]+".mp3", new_folder_path)
        if os.path.exists(file_path[:-4]+".wav"):
            shutil.move(file_path[:-4]+".wav", new_folder_path)


print("All .flp files have been moved into their respective folders.")

