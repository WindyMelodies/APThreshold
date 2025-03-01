import os
import re

def find_chinese_comments(directory):
    chinese_pattern = re.compile(r'#.*[\u4e00-\u9fff]+.*')
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    for line_num, line in enumerate(f, 1):
                        if chinese_pattern.search(line):
                            print(f'File: {filepath}, Line: {line_num}: {line.strip()}')

if __name__ == '__main__':
    project_directory = '..'
    find_chinese_comments(project_directory)