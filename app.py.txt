from flask import Flask
app = Flask(_name_)

@app.route('/')
def home():
    return "Hello from Flask on Render!"

if _name_ == '_main_':
    app.run()