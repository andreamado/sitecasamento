from os import system
from glob import glob

folder = 'mustache/'

for file in glob(f"{folder}*.html"):
    basename = file[len(folder):-5]
    system(f'mustache -p {folder}navbar.mustache {folder}data/{basename}.json {file} > {basename}.html')
    print(f'created {basename}.html')