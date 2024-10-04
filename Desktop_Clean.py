import os
import shutil

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
images_folder = os.path.join(desktop_path, "Images")
pdfs_folder = os.path.join(desktop_path, "PDF")
word_folder = os.path.join(desktop_path, "Word")

os.makedirs(images_folder, exist_ok=True)
os.makedirs(pdfs_folder, exist_ok=True)
os.makedirs(word_folder, exist_ok=True)

for filename in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, filename)
    if os.path.isfile(file_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            shutil.move(file_path, images_folder)
        elif filename.lower().endswith('.pdf'):
            shutil.move(file_path, pdfs_folder)
        elif filename.lower().endswith('.docx'):
            shutil.move(file_path, word_folder)
print("Dosyalar başarıyla ayrıldı!")
