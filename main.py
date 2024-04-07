import os

def delete_md_files():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                os.remove(os.path.join(root, file))

delete_md_files()


