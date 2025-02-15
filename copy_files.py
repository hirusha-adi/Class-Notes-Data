import os
import shutil

# Destination directory
dst = r"/srv/hirusha-class-notes/pocketbase/pb_public"

# Show a message to the user
print("Starting the process...")

# Step 1: Deleting everything inside the destination folder
print(f"1. Deleting everything inside the '{dst}' folder")
for filename in os.listdir(dst):
    file_path = os.path.join(dst, filename)
    print(f"1.X Now removing: {file_path}")
    if os.path.isdir(file_path):
        shutil.rmtree(file_path)
    else:
        os.remove(file_path)

# Step 2: Copying the './images' folder to the destination
print("2. Copying the './images' folder to '{}'".format(dst))
shutil.copytree('./images', os.path.join(dst, 'images'))

# Step 3: Copying the './subjects' folder to the destination
print("3. Copying the './subjects' folder to '{}'".format(dst))
shutil.copytree('./subjects', os.path.join(dst, 'subjects'))

# Success
print("Process completed successfully!")
