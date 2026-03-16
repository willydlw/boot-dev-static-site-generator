import os
from markdown_blocks import markdown_to_html_node 

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip() 
    raise Exception("No h1 header found in markdown")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # 1. Read markdown and template files 
    with open(from_path, "r") as f:
        markdown_content = f.read() 

    with open(template_path, "r") as f:
        template_content = f.read() 
    
    # 2. Convert markdown to HTML string 
    node = markdown_to_html_node(markdown_content)
    html_content = node.to_html() 

    # 3. Extract the title 
    title = extract_title(markdown_content)

    # 4. Replace placeholders 
    # Using .replace() is simple and effective for these two tags 
    full_html = template_content.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)

    # Replace root paths with the configurable basepath
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')

    # 5. Write to destination (creating directories if needed)
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(full_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            if from_path.endswith(".md"):
                # Use .replace(".md", ".html") for the dest_path
                generate_page(from_path, template_path, dest_path.replace(".md", ".html"), basepath)
        else:
            # Ensure the directory exists in public before recursing
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(from_path, template_path, dest_path, basepath)

