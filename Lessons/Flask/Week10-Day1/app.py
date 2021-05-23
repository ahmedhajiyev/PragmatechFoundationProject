from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return 'Home Page '

@app.route('/about')
def home():
    return 'This is about page '

@app.route('/news')
def home():
    return 'This is news page '

if __name__ == "__main__":
    app.run(debug=True)