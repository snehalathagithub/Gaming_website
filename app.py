# # app.py
from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

# Define the path to your scripts directory
SCRIPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_game', methods=['POST'])
def run_game():
    game_name = request.form['game']
    script_path = os.path.join(SCRIPTS_DIR, game_name)
    try:
        # Capture both stdout and stderr
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        output = result.stdout + result.stderr
    except Exception as e:
        output = str(e)
    return render_template('index.html', result=output)

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for
# import subprocess
# import os

# app = Flask(__name__)

# # Define the path to your scripts directory
# SCRIPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/run_game', methods=['POST'])
# def run_game():
#     game_name = request.form['game']
#     script_path = os.path.join(SCRIPTS_DIR, game_name)
#     try:
#         # Capture both stdout and stderr
#         result = subprocess.run(['python', script_path], capture_output=True, text=True)
#         output = result.stdout + result.stderr
#     except Exception as e:
#         output = str(e)
#     return redirect(url_for('game_output', output=output))

# @app.route('/output')
# def game_output():
#     output = request.args.get('output', '')
#     return render_template('output.html', result=output)

# if __name__ == '__main__':
#     app.run(debug=True)

