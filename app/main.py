#!/usr/bin/env python3
from flask import Flask, render_template, send_from_directory
import os
import random

app = Flask(__name__)

CITAZIONI_404 = [
    "Come i Cavalieri di Alabastro, hai smarrito la via...",
    "La Loggia Lumen Mentis ha confuso le tracce...",
    "Il Decodificatore Templare resta nascosto...",
    "Anche gli antichi Romani sbagliavano strada sulla Via Appia...",
    "Il Vaso di Alabastro non si trova in questo percorso...",
    "Le colline d'Irpinia custodiscono segreti, ma non questa pagina...",
]

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', citazione=random.choice(CITAZIONI_404)), 404

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('404.html', citazione=random.choice(CITAZIONI_404)), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
