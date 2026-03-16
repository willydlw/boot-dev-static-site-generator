import os 
import shutil 
import sys

from gencontent import generate_page, extract_title, generate_pages_recursive

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
"""
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
"""

"""
def main():
    source_static = "static"
    destination_public = "public"
    
    print("Cleaning and copying static files...")
    copy_static_to_public(source_static, destination_public)
    
    print("Generating all pages recursively...")
    generate_pages_recursive("content", "template.html", "public")
    
    print("Build complete! All pages generated.")
""" 

"""
def main():
    # Grab basepath from CLI, default to "/"
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_static_to_public("static", "public")
    
    # Pass basepath down the chain
    generate_pages_recursive("content", "template.html", "public", basepath)
""" 

def main():
    # Grab basepath from CLI, default to "/"
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    # Change destination from "public" to "docs"
    source_static = "static"
    destination_docs = "docs"
    
    print(f"Cleaning and copying static files to {destination_docs}...")
    copy_static_to_public(source_static, destination_docs)
    
    print(f"Generating all pages recursively to {destination_docs} with basepath '{basepath}'...")
    generate_pages_recursive("content", "template.html", destination_docs, basepath)
    
    print("Build complete! Site is ready for GitHub Pages in the /docs directory.")


if __name__ == "__main__":
    main()


