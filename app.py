from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Render!"

if _name_ == '__main__':
    app.run()