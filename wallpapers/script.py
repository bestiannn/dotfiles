# script for generate images for readme.md
import os

directory = os.path.dirname(os.path.abspath(__file__))
for root, dirs, files in os.walk(directory):
    for file in files:
        if not (file.endswith('.py') or file.endswith('.md')):
            print(f'![{}]({file})')