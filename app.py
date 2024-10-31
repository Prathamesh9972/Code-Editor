from flask import Flask, render_template, request, redirect, url_for, jsonify
from problems import problems, add_problem
from code_execution import execute_code
import os  

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/problems')
def problem_list():
    return render_template('problem_list.html', problems=problems)

@app.route('/problem/<int:problem_id>')
def problem_detail(problem_id):
    problem = next((p for p in problems if p['id'] == problem_id), None)
    if problem is None:
        return "Problem not found", 404
    return render_template('problem_detail.html', problem=problem)

@app.route('/add_problem', methods=['GET', 'POST'])
def add_problem_route():
    if request.method == 'POST':
        new_problem = {
            'title': request.form['title'],
            'description': request.form['description'],
            'test_cases': request.form['test_cases'].split('\n'),
            'expected_outputs': request.form['expected_outputs'].split('\n')
        }
        add_problem(new_problem)
        return redirect(url_for('problem_list'))
    return render_template('add_problem.html')

@app.route('/code_playground')
def code_playground():
    return render_template('code_playground.html')

@app.route('/execute_playground', methods=['POST'])
def execute_playground():
    code = request.json['code']
    language = request.json['language']
    input_data = request.json['input']

    output = execute_code(code, language, input_data)

    return jsonify({"output": output})

@app.route('/contest/<int:contest_id>/problems')
def contest_problems(contest_id):
    contest_name = f"Contest {contest_id}"
    problems = fetch_contest_problems(contest_id)
    return render_template('contest_problems.html', contest_name=contest_name, problems=problems)

def fetch_contest_problems(contest_id):
    example_problems = [
        {'id': 1, 'title': 'Two Sum', 'description': 'Find two numbers that add up to a target value.'},
        {'id': 2, 'title': 'Reverse Linked List', 'description': 'Reverse a linked list.'},
    ]
    return example_problems

@app.route('/contests')
def contests():
    return render_template('contests.html')

@app.route('/execute', methods=['POST'])
def execute():
    code = request.json['code']
    language = request.json['language']
    problem_id = request.json['problem_id']
    problem = next((p for p in problems if p['id'] == problem_id), None)
    if problem is None:
        return jsonify({"error": "Problem not found"}), 404

    results = []
    for test_case, expected_output in zip(problem['test_cases'], problem['expected_outputs']):
        output = execute_code(code, language, test_case)
        is_correct = output.strip() == expected_output.strip()
        results.append({
            "input": test_case,
            "expected_output": expected_output,
            "actual_output": output,
            "is_correct": is_correct
        })

    return jsonify(results)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
