import os
import shutil

# सही path यहाँ डालो
source = r"C:\Users\hakis\OneDrive\Desktop\test_folder"

images_folder = os.path.join(source, "Images")
pdf_folder = os.path.join(source, "PDFs")

os.makedirs(images_folder, exist_ok=True)
os.makedirs(pdf_folder, exist_ok=True)

for file in os.listdir(source):
    file_path = os.path.join(source, file)

    if os.path.isfile(file_path):

        if file.endswith(".jpg"):
            shutil.move(file_path, os.path.join(images_folder, file))

        elif file.endswith(".pdf"):
            shutil.move(file_path, os.path.join(pdf_folder, file))

print("✅ Files Organized Successfully")