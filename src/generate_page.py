
import os

from markdownblock import markdown_to_html_node

def extract_title(markdown:str):
    lines = markdown.split("\n")
    first_line = lines[0]
    if not first_line.startswith("# "):
        raise Exception("Missing title!")
    return first_line[2:].strip()

def generate_page(base_path:str, from_path:str, template_path:str, dest_path:str):
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
    final_content = final_content.replace('href="/',f'href="{base_path}')
    final_content = final_content.replace('src="/',f'src="{base_path}')

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    with open(dest_path, "w") as file:
        file.write(final_content)

def generate_pages_recursive(base_path:str, dir_path_content:str, template_path:str, dest_dir_path:str):
    if not os.path.exists(dir_path_content):
        raise Exception("content path is not valid")
    if not os.path.exists(template_path):
        raise Exception("tempalte path is not valid")
    for item in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, item)
        target_path = os.path.join(dest_dir_path, item)
        if os.path.isdir(from_path):
            generate_pages_recursive(base_path, from_path, template_path, target_path)
            continue
        if os.path.isfile(from_path) and from_path.endswith(".md"):
            generate_page(base_path, from_path, template_path, target_path.replace(".md",".html"))



    
