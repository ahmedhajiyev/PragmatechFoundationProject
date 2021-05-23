from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return 'Home Page '

@app.route('/about')
def home():
    return 'This is about page '



if __name__ == "__main__":
    app.run(debug=True)