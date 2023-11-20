import os

def generate_yaml(folder_path, yaml_file):
    with open(yaml_file, 'w') as file:
        file.write('photos:\n')
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                file.write(f"- url: \"../assets/images/photos/{filename}\"\n")

folder_path = '../assets/images/photos'  # 指定文件夹的路径
yaml_file = 'photos.yml'  # 输出YAML文件的名称
generate_yaml(folder_path, yaml_file)
