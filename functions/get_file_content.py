import os

from google.genai import types

from config import MAX_FILE_READ_SIZE


def get_file_content(working_directory, file_path):
    try:
        working_dir = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir, file_path))

        target_path_in_working_dir = (
            os.path.commonpath((working_dir, target_path)) == working_dir
        )
        if not target_path_in_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_path) as file:
            file_content = file.read(MAX_FILE_READ_SIZE)
            if file.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_FILE_READ_SIZE} characters]'

        return file_content
    except Exception as err:
        return f"Error: {err}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Read the first {MAX_FILE_READ_SIZE} characters of a file. If a file is larger than that, a truncation note is appended to the end of the response.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to file to read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)
