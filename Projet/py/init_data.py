# -*- coding: utf-8 -*-
"""
Ce module initialise les données en obtenant la liste des thèmes et des ensembles
à partir de l'API et en les enregistrant dans des fichiers.
Utile pour éviter de faire trop de requêtes à l'API.
"""
import os
import json
import brickse

import api_interact as api_utils

FICHIER = './data/'


def save_json_to_file(data, path_data):
    """
    Enregistrer les données dans un fichier
    """
    path_script = os.path.dirname(__file__)
    path_file = os.path.join(path_script, FICHIER)

    # Vérifier si le fichier existe
    if not os.path.exists(path_file):
        if not os.path.exists(path_file):
            os.makedirs(path_file)
        # Créer le fichier s'il n'existe pas
        with open(path_data, 'w', encoding='utf-8') as fichier:
            json.dump(data, fichier)
        return

    # Écrire les données dans le fichier
    with open(path_data, 'w', encoding='utf-8') as fichier:
        json.dump(data, fichier)


def init_themes(filename='themes'):
    """
    Obtenir la liste des thèmes
    """
    filename = f'{filename}.json'
    path_script = os.path.dirname(__file__)
    path_file = os.path.join(path_script, FICHIER)
    path_data = os.path.join(path_file, filename)

    # Vérifier si le fichier existe et si les thèmes sont déjà enregistrés
    if os.path.exists(path_data) and json.loads(brickse.lego.get_themes().read()) != []:
        print("Les thèmes sont déjà enregistrés.")
        return

    themes = json.loads(brickse.lego.get_themes().read())['themes']
    save_json_to_file(themes, path_data)


def init_sets(filename='sets'):
    """
    Obtenir la liste des ensembles
    """
    filename = f'{filename}.json'
    path_script = os.path.dirname(__file__)
    path_file = os.path.join(path_script, FICHIER)
    path_data = os.path.join(path_file, filename)
    if os.path.exists(path_data):
        with open(path_data, 'r', encoding='utf-8') as fichier:
            try:
                liste_sets = json.load(fichier)
                if liste_sets:
                    if liste_sets == []:
                        return
            except json.JSONDecodeError:
                pass
    else:
        save_json_to_file([], path_data)


def main():
    """
    Initialiser les données
    """
    for key_api in api_utils.API_KEY.copy():
        api_utils.init(key_api)
        try:
            # Inilialiser les thèmes
            init_themes()
            # Initialiser les ensembles sur une liste vide
            init_sets()
            break
        except KeyError:
            print("Nombre de requêtes dépassé, changement de clé API")
            if key_api == api_utils.API_KEY[-1]:
                print("Nombre de requêtes dépassé pour toutes les clés API")
                return
            else:
                api_utils.API_KEY.remove(key_api)

    choix = input("Faire fonctionner le site avec les images en local ? ([o]/n) : ")
    while choix.lower() not in ['o', 'n', '']:
        choix = input("Faire fonctionner le site avec les images en local ? ([o]/n) : ")
    if choix.lower() in ['o', '']:
        api_utils.DOWNLOAD_IMG = True


if __name__ == '__main__':
    main()
