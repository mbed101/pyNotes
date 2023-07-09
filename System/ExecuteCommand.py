#! /usr/bin/env python3
import subprocess

# Execute a shell command and capture its output
def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, 
                                         universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        # Handle command execution errors
        print(f"Command execution failed with return code {e.returncode}: {e.output}")
        return None

# Example usage
command = "ls -l"
output = execute_command(command)
if output:
    print(f"Command output:\n{output}")