#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask, request
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

    return f'\
        <h3>Hello, {name}!</h3>\
        <a href="javascript:history.back()">back<a>'
