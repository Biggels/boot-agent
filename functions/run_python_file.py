import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir, file_path))

        target_path_in_working_dir = (
            os.path.commonpath((working_dir, target_path)) == working_dir
        )
        if not target_path_in_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_path]
        if args:
            command.extend(args)

        process = subprocess.run(
            command, cwd=working_dir, capture_output=True, text=True, timeout=30
        )

        output = ""
        if process.returncode != 0:
            output += "Process exited with code X"
        if not process.stdout and not process.stderr:
            output += "No output produced"
        output += f"STDOUT: {process.stdout}"
        output += f"STDERR: {process.stderr}"
        return output

    except Exception as err:
        return f"Error: executing Python file: {err}"
