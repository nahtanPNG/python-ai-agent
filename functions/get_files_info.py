import os


def get_files_info(working_directory, directory=None):
    working_directory = os.path.abspath(working_directory)
    if directory is None:
        directory = working_directory
    elif not os.path.isabs(directory):
        directory = os.path.abspath(os.path.join(working_directory, directory))
    else:
        directory = os.path.abspath(directory)

    if directory.startswith(working_directory):
        if not os.path.isdir(directory):
            print(f'Error: "{directory}" is not a directory')
            return
        files = ""
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            files += f"{file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}\n"
        return files
    else:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return
