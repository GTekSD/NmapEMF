import os

list_file = 'list.txt'
created_count = 0
skipped_count = 0
error_count = 0

if not os.path.exists(list_file):
    print(f'List file {list_file} not found.')
    exit(1)

with open(list_file, 'r') as f:
    for path in f.readlines():
        path = path.strip()
        parent_dir = os.path.dirname(path)
        try:
            os.makedirs(parent_dir, exist_ok=True)
            os.makedirs(path, exist_ok=True)
            print(f'Created directory: {path}')
            created_count += 1
        except OSError as e:
            print(f'Error creating directory {path}: {e}')
            error_count += 1
        except FileExistsError:
            print(f'Skipped existing directory: {path}')
            skipped_count += 1

print(f'\nDirectories created: {created_count}')
print(f'Directories skipped: {skipped_count}')
print(f'Directory creation errors: {error_count}')
