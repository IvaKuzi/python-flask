#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    return app.send_static_file("home.html")

@app.route("/about")
def about():
    return app.send_static_file("about.html")

@app.route("/contact")
def contact():
    return app.send_static_file("contact.html")

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    print(f"Hello {name}!")

    # Open a file named 'submissions.txt' in append mode ('w')
    with open('submissions.txt', 'a') as file:
        # Write a string to the file
        file.write((f"Hello {name}!\n"))
    '''
    # variant 1: inline approach 
    return f'\
        <h3>Hello, {name}!</h3>\
        <a href="javascript:history.back()">back<a>'
    '''
    # variant 2: template (requires render_template)
    return render_template('hello.html', name=name)


@app.route("/log")
def submissions_log():
    content = '<h1>Submissions Log</h1>'
    filename = "submissions.txt"
    
    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            lines = file.readlines()  # Read each line as a list, keeping the '\n'
            for line in lines:
                print(line)    # Print each line, keeping the newline characters
                content = content + f'<p>{line}</p>'
    except FileNotFoundError:
        # Handle the error if the file doesn't exist
        content = content + f"The file '{filename}' does not exist."
    
    content = content + '<a href="javascript:history.back()">back<a>'
    
    print(content)
    return content

'''
@app.route("/<name>")
def hello(name):
    return f"<p>Page <b>{escape(name)}</b> not found!</p>"
'''

