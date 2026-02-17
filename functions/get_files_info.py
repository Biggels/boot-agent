import os

from google.genai import types


def get_files_info(working_directory, directory="."):
    try:
        working_dir = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir, directory))

        target_path_in_working_dir = (
            os.path.commonpath((working_dir, target_path)) == working_dir
        )
        if not target_path_in_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_path):
            return f'Error: "{directory}" is not a directory'

        file_names = os.listdir(target_path)
        files_info = []
        for name in file_names:
            path = os.path.join(target_path, name)
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


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (optional, default is the working directory itself)",
            ),
        },
        required=[],
    ),
)
