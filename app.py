from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        with open("test.txt", "w") as file:
            file.write("TESTE")

        return 'Hello, world!'
        
    except Exception as err: return str(err)
    
    
