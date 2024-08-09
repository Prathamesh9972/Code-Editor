import sys
from io import StringIO
import subprocess
import tempfile
import os


def execute_code(code, language, input_data):
    if language == 'python':
        try:
            process = subprocess.Popen(['python', '-c', code],
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       text=True)
            stdout, stderr = process.communicate(input=input_data)
            if stderr:
                return f"Error: {stderr}"
            return stdout
        except Exception as e:
            return f"Error: {str(e)}"
    elif language == 'javascript':
        try:
            process = subprocess.Popen(['node', '-e', code],
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       text=True)
            stdout, stderr = process.communicate(input=input_data)
            if stderr:
                return f"Error: {stderr}"
            return stdout
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "Unsupported language"


def execute_python(code, input_data):
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    redirected_input = sys.stdin = StringIO(input_data)
    redirected_output = sys.stdout = StringIO()

    try:
        exec(code)
        sys.stdin = old_stdin
        sys.stdout = old_stdout
        return redirected_output.getvalue()
    except Exception as e:
        sys.stdin = old_stdin
        sys.stdout = old_stdout
        return str(e)


def execute_javascript(code, input_data):
    try:
        result = subprocess.run(['node', '-e', f"{code}\nconsole.log(twoSum({input_data}))"], capture_output=True,
                                text=True, timeout=5)
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return "Execution timed out"
    except Exception as e:
        return str(e)


def execute_cpp(code, input_data):
    with tempfile.TemporaryDirectory() as tmpdir:
        cpp_file = os.path.join(tmpdir, "code.cpp")
        exe_file = os.path.join(tmpdir, "code.exe")

        full_code = f"""
#include <iostream>
#include <vector>
using namespace std;

{code}

int main() {{
    {input_data}
    vector<int> result = twoSum(nums, target);
    cout << "[" << result[0] << "," << result[1] << "]" << endl;
    return 0;
}}
"""

        with open(cpp_file, "w") as f:
            f.write(full_code)

        try:
            # Compile
            compile_result = subprocess.run(['g++', cpp_file, '-o', exe_file], capture_output=True, text=True,
                                            timeout=5)
            if compile_result.returncode != 0:
                return f"Compilation error:\n{compile_result.stderr}"

            # Run
            run_result = subprocess.run([exe_file], capture_output=True, text=True, timeout=5)
            return run_result.stdout + run_result.stderr
        except subprocess.TimeoutExpired:
            return "Execution timed out"
        except Exception as e:
            return str(e)