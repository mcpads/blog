import shutil
import os
# For given directory, change all markdown file names to
# YYYY-MM-DD-title.md format, where date and title in jekyll format

def copy_file(file_path, file_name):
    with open(os.path.join(file_path, file_name), 'r') as file:
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
            if not os.path.exists(os.path.join(target_file_dir, new_file_name)):
                shutil.copyfile(os.path.join(file_path, file_name),
                                os.path.join(target_file_dir, new_file_name))
            else:
                raise Exception("File already exists: " + new_file_name)


def copy_files(file_path):
    for file_name in os.listdir(file_path):
        if file_name.endswith('.md'):
            copy_file(file_path, file_name)
        if os.path.isdir(os.path.join(file_path, file_name)):
            copy_files(os.path.join(file_path, file_name))

my_path = os.path.abspath(os.path.dirname(__file__))
target_file_dir = os.path.join(my_path, '../_posts/')
original_file_dir = os.path.join(my_path, '../posts/')

if __name__ == '__main__':
    if not os.path.exists(target_file_dir):
        os.makedirs(target_file_dir)
    copy_files(original_file_dir)
