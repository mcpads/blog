import sys
import os
# For given directory, change all markdown file names to
# YYYY-MM-DD-title.md format, where date and title in jekyll format

my_path = os.path.abspath(os.path.dirname(__file__))

file_path = os.path.join(my_path, '../_posts/')

markdown_files = [f for f in os.listdir(file_path) if f.endswith('.md')]

for f in markdown_files:
    with open(os.path.join(file_path, f), 'r') as file:
        file_content = file.readlines()
        title, datetime = None, None
        for line in file_content:
            if line.startswith('title: '):
                title = line[7:].strip()
            if line.startswith('date: '):
                datetime = line[6:].strip()
            if title is not None and datetime is not None:
                break
        if title is not None and datetime is not None:
            title = title.replace(' ', '-')
            date = datetime.split(' ')[0]
            new_file_name = date + '-' + title + '.md'
            if new_file_name != f:
                print(f, " -> ", new_file_name)
                if not os.path.exists(os.path.join(file_path, new_file_name)):
                    os.rename(os.path.join(file_path, f),
                              os.path.join(file_path, new_file_name))
                else:
                    print('File already exists: ', new_file_name)
