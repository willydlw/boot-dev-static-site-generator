import os 
import shutil 

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
    print("Copying static files to public directory...")
    copy_static_to_public("static", "public")

    # Later, you'll add your markdown_to_html_node logic here 
    # to generate the actual index.html file!

if __name__ == "__main__":
    main()
