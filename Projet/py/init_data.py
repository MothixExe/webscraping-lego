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


def save_json_to_file(data, filename):
    """
    Enregistrer les données dans un fichier
    """
    # Vérifier si le fichier existe
    if not os.path.exists(filename):
        if not os.path.exists(FICHIER):
            os.makedirs(FICHIER)
        # Créer le fichier s'il n'existe pas
        with open(filename, 'w', encoding='utf-8') as fichier:
            json.dump(data, fichier)
        return

    # Écrire les données dans le fichier
    with open(filename, 'w', encoding='utf-8') as fichier:
        json.dump(data, fichier)


def init_themes(filename='themes'):
    """
    Obtenir la liste des thèmes
    """
    themes = json.loads(brickse.lego.get_themes().read())['themes']
    save_json_to_file(themes, f'{FICHIER}{filename}.json')


def init_sets(filename='sets'):
    """
    Obtenir la liste des ensembles
    """
    filename = f'{FICHIER}{filename}.json'
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as fichier:
            try:
                liste_sets = json.load(fichier)
                if liste_sets:
                    if liste_sets == []:
                        return
            except json.JSONDecodeError:
                pass
    else:
        save_json_to_file([], filename)


def main():
    """
    Initialiser les données
    """
    api_utils.init(api_utils.API_KEY)

    # Inilialiser les thèmes
    init_themes()
    # Initialiser les ensembles sur une liste vide
    init_sets()


if __name__ == '__main__':
    main()
