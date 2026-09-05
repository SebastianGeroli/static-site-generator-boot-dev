
import os

from markdownblock import markdown_to_html_node

def extract_title(markdown:str):
    lines = markdown.split("\n")
    first_line = lines[0]
    if not first_line.startswith("# "):
        raise Exception("Missing title!")
    return first_line[2:].strip()

def generate_page(from_path:str, template_path:str, dest_path:str):
    print(f"Generating page from: {from_path} to {dest_path} using {template_path}")
    markdown_content:str = ""
    template_content:str = ""
    with open(from_path, "r") as file:
        markdown_content = file.read()
    with open(template_path, "r") as file:
        template_content = file.read()
    html = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    final_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}",html)
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    with open(dest_path, "w") as file:
        file.write(final_content)

    

    
