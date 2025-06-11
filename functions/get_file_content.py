import os


def get_file_content(working_directory, file_path):
    working_directory = os.path.abspath(working_directory)
    if file_path is None:
        file_path = working_directory
    elif not os.path.isabs(file_path):
        file_path = os.path.abspath(os.path.join(working_directory, file_path))
    else:
        file_path = os.path.abspath(file_path)

    if file_path.startswith(working_directory):
        if not os.path.isfile(file_path):
            print(f'Error: File not found or is not a regular file: "{file_path}"')
            return
        MAX_CHARS = 10000

        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        
        if len(file_content_string) == MAX_CHARS:
            file_content_string += f'\n "{file_path}" truncated at 10000 characters'
        return file_content_string

    else:
        print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        return