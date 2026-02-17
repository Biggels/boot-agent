import os


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
