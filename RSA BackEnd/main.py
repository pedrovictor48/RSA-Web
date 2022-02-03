from flask import Flask, jsonify, request
from itsdangerous import json
from functions import *
from functions.criptografia import desencriptar, encriptar
from functions.number_theory import ehPrimo
import math
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/encriptar', methods=["POST"])
def func():
    if request.method == "POST":
        data = request.get_json()
        msg, N, E = data["msg"], int(data["N"]), int(data["E"])
        return jsonify({
            "msg": encriptar(msg, N, E)
        })

@app.route('/desencriptar', methods=["POST"])
def func2():
    if request.method == "POST":
        data = request.get_json()
        msg, P, Q, E = data["msg"], int(data["P"]), int(data["Q"]), int(data["E"])
        return jsonify({
            "msg": desencriptar(msg, P, Q, E)
        })

@app.route('/gerar', methods=["POST"])
def func3():
    if request.method == "POST":
        data = request.get_json()
        P, Q, E = int(data["P"]), int(data["Q"]), int(data["E"])

        if not ehPrimo(P):
            response = jsonify({
                "erro": 1,
                "msg": f"P ({P}) is not prime"
            })
        elif not ehPrimo(Q):
            response = jsonify({
                "erro": 1,
                "msg": f"Q ({Q}) is not prime"
            })
        elif math.gcd((P - 1) * (Q - 1), E) != 1:
            response = jsonify({
                "erro": 1,
                "msg": f"E ({E}) is not coprime with (P - 1)*(Q - 1) ({(P - 1) * (Q - 1)})"
            })
        else:
            response = jsonify({
                "erro": 0,
                "N": P*Q,
                "E": E
            })
        return response