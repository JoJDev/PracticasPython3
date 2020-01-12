from flask import Flask

app = Flask(__name__);

@app.route('/')
def main():
    return "Hola mundo, este es un servidor con Python3 :)";


if __name__ == "__main__":
    app.run();