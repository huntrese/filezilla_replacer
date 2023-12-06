import os

def modify_files(old,new):
    for dirpath, dirnames, filenames in os.walk('indexes'):
        for dir in dirnames:
            
            with open(f"indexes\\{dir}\\index.php","r",encoding="UTF-8") as f:
                d=f.read()
                updated_paths=[f"updated_indexes\\{dir}\\index.php"]
                for updated_path in updated_paths:
                    os.makedirs(os.path.dirname(updated_path), exist_ok=True)
                    with open(updated_path,"w",encoding="UTF-8") as file:
                        d=d.replace(old,new)
                        file.write(d)
            