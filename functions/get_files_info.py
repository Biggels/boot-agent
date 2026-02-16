import os


def get_files_info(working_directory, directory="."):
    try:
        working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir, directory))

        target_dir_is_in_working_dir = (
            os.path.commonpath((working_dir, target_dir)) == working_dir
        )
        if not target_dir_is_in_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        file_names = os.listdir(target_dir)
        files_info = []
        for name in file_names:
            path = os.path.join(target_dir, name)
            size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            files_info.append({"name": name, "size": size, "is_dir": is_dir})

        response = "\n".join(
            f"- {file['name']}: file_size={file['size']} bytes, is_dir={file['is_dir']}"
            for file in files_info
        )
        return response

    except Exception as err:
        return f"Error: {err}"
