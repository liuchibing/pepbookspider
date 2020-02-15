import json
import sys
import os
import pathlib
import pepbookspider.settings as settings

f = open(sys.argv[1])

books = json.load(f)

os.chdir(settings.FILES_STORE)

for file in books:
    file_name = file.get('file_names')[0]
    actual_path = file['files'][0]['path']
    dest_path = os.path.split(actual_path)[0]
    dest_path = os.path.join(dest_path, file_name + '.pdf')
    print(actual_path, "=>", dest_path)
    os.rename(actual_path, dest_path)

print(len(books), "file(s).")