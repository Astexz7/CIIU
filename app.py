from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Centro da Informação de Infraestrutura Universitária!"

if __name__ == '__main__':
    app.run(debug=True)