import os
import subprocess

from google.genai import types


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


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python file with optional args. Command is structured as: python <file_path> [args...]. Returns a formatted summary of the output including possible non-zero exit codes, STDOUT, and/or STDERR.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="List of arguments to pass to the python file you're running. Default is None.",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)
