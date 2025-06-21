import os, shutil

source_dirs = ["dataset/vid-1", "dataset/vid-2", "dataset/vid-3"]
image_out = "dataset/images"
label_out = "dataset/labels"

os.makedirs(image_out, exist_ok=True)
os.makedirs(label_out, exist_ok=True)

for src in source_dirs:
    for file in os.listdir(src):
        src_path = os.path.join(src, file)
        if file.endswith(".jpg"):
            shutil.copy(src_path, os.path.join(image_out, file))
        elif file.endswith(".txt"):
            shutil.copy(src_path, os.path.join(label_out, file))
