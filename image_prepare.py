import os
import shutil
from datetime import datetime, timedelta
import getpass

# #### Delete the contents of a folder
def delete_image():
    folder = 'images'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    print("Images delete sucessfully")


#####  Copy all image files generated in the last two minutes from one folder to another
def copy_image(period):
    count = 0
    user = getpass.getuser()
    dst_dir = 'images'
    src_dir = 'C:/Users/'+user+'/Downloads'  ### The default downloading folder of Chrome
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    now = datetime.now()
    time_delta = now - timedelta(minutes=int(period))
    for filename in os.listdir(src_dir):
        file_path = os.path.join(src_dir, filename)
        if os.path.isfile(file_path) and os.path.splitext(filename)[1].lower() in image_extensions:
            file_timestamp = datetime.fromtimestamp(os.path.getctime(file_path))
            if file_timestamp > time_delta:
                count += 1
                shutil.copy(file_path, dst_dir)
    print("Images copied successfully.")
    return count



