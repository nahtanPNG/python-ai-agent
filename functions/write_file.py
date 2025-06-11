import os


def write_file(working_directory, file_path, content):
    working_directory = os.path.abspath(working_directory)
    if file_path is None:
        file_path = working_directory
    elif not os.path.isabs(file_path):
        file_path = os.path.abspath(os.path.join(working_directory, file_path))
    else:
        file_path = os.path.abspath(file_path)
    
    if file_path.startswith(working_directory):
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                 f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return f'Error: {str(e)}'
    

    else:
        print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        return