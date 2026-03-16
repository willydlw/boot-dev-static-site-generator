import os
from markdown_blocks import markdown_to_html_node 

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip() 
    raise Exception("No h1 header found in markdown")

def generate_page(from_path, template_path, dest_path):
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

    # 5. Write to destination (creating directories if needed)
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(full_html)
