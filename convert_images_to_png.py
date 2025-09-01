import os
from PIL import Image

# Directory containing your images
img_dir = r'../'

# Supported extensions to convert
extensions = ['.jpg', '.jpeg', '.tiff', '.tif']

for filename in os.listdir(img_dir):
    name, ext = os.path.splitext(filename)
    if ext.lower() in extensions:
        img_path = os.path.join(img_dir, filename)
        out_path = os.path.join(img_dir, name.replace(' ', '_') + '.png')
        try:
            with Image.open(img_path) as img:
                img.save(out_path, 'PNG')
            print(f'Converted: {filename} -> {os.path.basename(out_path)}')
        except Exception as e:
            print(f'Failed to convert {filename}: {e}')
