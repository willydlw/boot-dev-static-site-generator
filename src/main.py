import os 
import shutil 

from gencontent import generate_page, extract_title

def copy_static_to_public(source, destination):
    # 1. clean the destination 
    if os.path.exists(destination):
        print(f"Cleaing {destination}...")
        shutil.rmtree(destination)

    print(f"Creating {destination}...")
    os.mkdir(destination)

    # 2. Start the recursive copy 
    _copy_recursive(source, destination)

def _copy_recursive(src, dst):
    # get all files/folders in the current source directory 
    items = os.listdir(src)

    for item in items:
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)
        else:
            print(f"Creating directory: {dst_path}")
            os.mkdir(dst_path)
            # recursively call for the subdirectory 
            _copy_recursive(src_path, dst_path)

def main():
    # 1. Clean and Copy static assets 
    source_static = "static"
    destination_public = "public"

    print("Cleaning and copying static files...")
    copy_static_to_public(source_static, destination_public)

    # 2. Generate the index page 
    from_path = "content/index.md"
    template_path = "template.html"
    dest_path = "public/index.html"

    print(f"Generating page from {from_path} to {dest_path}...")
    generate_page(from_path, template_path, dest_path)

    print("Build complete!")


if __name__ == "__main__":
    main()
