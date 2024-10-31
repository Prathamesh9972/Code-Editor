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
    elif language == 'java':
        return execute_java(code, input_data)
    elif language == 'cpp':
        return execute_cpp(code, input_data)
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

def execute_java(code, input_data):
    with tempfile.TemporaryDirectory() as tmpdir:
        # Since Java requires the class name to match the file name,
        # we need to extract the class name from the code
        import re
        class_match = re.search(r'public\s+class\s+(\w+)', code)
        if not class_match:
            return "Error: Could not find public class name in Java code"
        
        class_name = class_match.group(1)
        java_file = os.path.join(tmpdir, f"{class_name}.java")
        
        # Write the Java code to a temporary file
        with open(java_file, "w") as f:
            f.write(code)
        
        try:
            # Compile Java code
            compile_result = subprocess.run(['javac', java_file], 
                                         capture_output=True, 
                                         text=True, 
                                         timeout=5)
            
            if compile_result.returncode != 0:
                return f"Compilation error:\n{compile_result.stderr}"
            
            # Run Java code
            run_result = subprocess.run(['java', '-cp', tmpdir, class_name],
                                      input=input_data,
                                      capture_output=True,
                                      text=True,
                                      timeout=5)
            
            if run_result.stderr:
                return f"Runtime error:\n{run_result.stderr}"
            
            return run_result.stdout
            
        except subprocess.TimeoutExpired:
            return "Execution timed out"
        except Exception as e:
            return str(e)

# Example usage for C++
if __name__ == "__main__":
    # Your C++ solution code
    cpp_code = """
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
    }
    """

    # Test Case 1
    input_data = """
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    """
    print("Test Case 1:")
    result = execute_code(cpp_code, 'cpp', input_data)
    print(result)  # Should print [0,1]

    # Test Case 2
    input_data = """
    vector<int> nums = {3, 2, 4};
    int target = 6;
    """
    print("\nTest Case 2:")
    result = execute_code(cpp_code, 'cpp', input_data)
    print(result)  # Should print [1,2]

    # Test Case 3
    input_data = """
    vector<int> nums = {3, 3};
    int target = 6;
    """
    print("\nTest Case 3:")
    result = execute_code(cpp_code, 'cpp', input_data)
    print(result)  # Should print [0,1]
