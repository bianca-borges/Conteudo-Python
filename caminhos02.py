import os
import shutil

caminho_original = r'C:\Users\bianc\OneDrive\Documents\Bianca'
caminho_novo = r'C:\Users\bianc\OneDrive\Documents\Bianca02'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    # print(f'Pasta {caminho_novo} ja existe.')
    pass

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if '.jpg' in file:
           # shutil.move(old_file_path, new_file_path)
            # shutil.copy(old_file_path, new_file_path)
            os.remove(new_file_path)
            print(f'Arquivo {file} apagado com sucesso.')
