import sys
import os

def get_shared_lib_name(lib_dir: str):
    lib_path = os.listdir(lib_dir)[0]
    return os.path.basename(lib_path)

def main(output_dir: str, project_name: str):
    template = """
    [configuration]

    entry_symbol = "main_library_init"
    compatibility_minimum = "4.1"
    reloadable = true

    [libraries]

    macos.debug = "res://bin/lib/macOS_PLACEHOLDER"
    """

    configs = {
        'macOS': 'Darwin-universal' 
    }
    lib_root = f'{output_dir}/lib'

    for k, v in configs.items():
        lib_dir = f'{lib_root}/{v}'
        lib_name = get_shared_lib_name(lib_dir)
        template = template.replace(f'{k}_PLACEHOLDER', f'{v}/{lib_name}')
        
    with open(f'{output_dir}/{project_name}.gdextension', 'w') as f:
        f.write(template)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main(sys.argv[1], sys.argv[2])