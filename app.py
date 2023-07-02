from flask import Flask
from flask_cors import CORS
from services import Tables

app = Flask(__name__)
CORS(app)

# @app.route('/heats', methods=['GET'])
# def get_table_1():
#     return Tables.fetch_all_data_from_table_1()

# @app.route('/enfermedades', methods=['GET'])
# def get_table_2():
#     return Tables.fetch_all_data_from_table_2()

@app.route('/hello_world', methods=['GET'])
def saludar():
    return "felicidades, creaste tu primer endpoint de flask"

@app.route('/holi', methods=['GET'])
def hello():
    return "holi"


if __name__ == '__main__':
    app.run()