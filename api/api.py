from flask import Flask, request, Response
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__) 

@app.route('/', methods=['POST'])
def api_func():
    # o json é passado como parâmetro no request!
    body = request.get_json()

    user, password, db  = 'postgres', 'postgres', 'postgres'
    engine = create_engine(f'postgresql://{user}:{password}@localhost:5432/{db}')    
    conn = engine.raw_connection()
    query = f"SELECT * FROM customers where customerid = {body['id']};"

    df = pd.read_sql_query(query, conn)
    return df.to_dict()


@app.route('/gdi', methods=['POST'])
def get_update_():
    return 'ok'


