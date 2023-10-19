from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():

    with open("test.txt", "w") as file:
        file.write("TESTE")
    
    return 'Hello, world!'
