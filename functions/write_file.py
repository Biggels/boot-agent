import os

from google.genai import types


def write_file(working_directory, file_path, content):
    try:
        working_dir = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir, file_path))

        target_path_in_working_dir = (
            os.path.commonpath((working_dir, target_path)) == working_dir
        )
        if not target_path_in_working_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_path), exist_ok=True)

        with open(target_path, "w") as file:
            file.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as err:
        return f"Error: {err}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write contents to a file. The file will be overwritten if it already exists. Parent directories will be created automatically.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file. Interpreted as text.",
            ),
        },
        required=["file_path", "content"],
    ),
)
