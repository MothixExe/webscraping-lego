# -*- coding: utf-8 -*-
"""
Ce module est destiné à exécuter le serveur Flask et à gérer les requêtes de l'application.
"""
from flask import Flask, request
from flask_cors import CORS

import api_interact as api

app = Flask(__name__)
CORS(app)


# Interaction concernant les thèmes
@app.route('/themes', methods=['GET', 'POST'])
def get_theme_name():
    """
    Obtenir la liste des thèmes
    """
    print(f'{request.method} pour themes')
    if request.method == 'GET':
        return api.get_themes_name()
    if request.method == 'POST':
        try:
            return {"statusCode": 200}
        except KeyError as exeption:
            print(exeption)
    return {"statusCode": 501}


# Interaction concernant les thèmes par année
@app.route('/theme/search/', methods=['GET', 'POST'])
def get_theme_name_filter():
    """
    Obtenir la liste des thèmes
    """
    print(f'{request.method} pour themes/search')
    if request.method == 'GET':
        yearfrom = request.args.get('yearFrom')
        yearto = request.args.get('yearTo')
        recherche_text = request.args.get('search')
        return api.get_themes_name(yearfrom=int(yearfrom),
                                   yearto=int(yearto), search=recherche_text)
    if request.method == 'POST':
        try:
            return {"statusCode": 200}
        except KeyError as exeption:
            print(exeption)
    return {"statusCode": 501}


# Interaction concernant les ensembles d'un thème
@app.route('/theme/<theme>', methods=['GET', 'POST'])
def get_set_by_theme(theme):
    """
    Obtenir la liste des thèmes
    """
    print(f'{request.method} pour theme/{theme}')
    if request.method == 'GET':
        return api.get_sets(theme)
    if request.method == 'POST':
        try:
            return {"statusCode": 200}
        except KeyError as exeption:
            print(exeption)
    return {"statusCode": 501}


# Interaction pour obtenir tous les ensembles lego
@app.route('/all_sets/search/', methods=['GET', 'POST'])
def get_all_sets_filter():
    """
    Obtenir la liste de tous les sets lego filtrés
    """
    print(f'{request.method} pour all_sets/search')
    if request.method == 'GET':
        recherche_text = request.args.get('search')
        return api.get_sets(all_sets=True, search=recherche_text)
    if request.method == 'POST':
        try:
            return {"statusCode": 200}
        except KeyError as exeption:
            print(exeption)
    return {"statusCode": 501}


# Interaction pour obtenir tous les ensembles lego filtrés
@app.route('/all_sets', methods=['GET', 'POST'])
def get_all_sets():
    """
    Obtenir la liste de tous les ensembles lego
    """
    print(f'{request.method} pour all_sets')
    if request.method == 'GET':
        return api.get_sets(all_sets=True)
    if request.method == 'POST':
        try:
            return {"statusCode": 200}
        except KeyError as exeption:
            print(exeption)
    return {"statusCode": 501}


# Interaction pour obtenir des informations sur un ensemble lego
@app.route('/set/<set_number>', methods=['GET', 'POST'])
def get_set_info(set_number):
    """
    Obtenir les informations sur un ensemble lego
    """
    print(f'{request.method} pour get_info')
    if request.method == 'GET':
        return api.get_set_info(set_number)
    if request.method == 'POST':
        try:
            return {"statusCode": 200}
        except KeyError as exeption:
            print(exeption)
    return {"statusCode": 501}


# Interaction poour obtenir des informations sur la base de données actuelle
@app.route('/db_info', methods=['GET', 'POST'])
def get_db_info():
    """
    Obtenir les informations sur la base de données actuelle
    """
    print(f'{request.method} pour db_info')
    if request.method == 'GET':
        return api.get_db_info()
    if request.method == 'POST':
        try:
            return {"statusCode": 200}
        except KeyError as exeption:
            print(exeption)
    return {"statusCode": 501}


def start_app():
    """
    Démarrer l'application
    """
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
    api.init(api.API_KEY)

if __name__ == '__main__':
    start_app()
