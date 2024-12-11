# -*- coding: utf-8 -*-
"""
Toutes les fonctions pour interagir avec l'API Brickse et répondre aux 
requêtes du serveur d'applications Flask.

Fait par Mothix et Matis
"""
import os
import json
import random
import datetime
from rapidfuzz import process, fuzz

import brickse
import utils
import init_data

# Clé d'API pour accéder à Brickset
# (limited to 100 requests per day)
API_KEY = ['3-7B1M-6WHA-JxOTZ', '3-8MeG-xlFh-ZlQgO']
# API_KEY = '3-7B1M-6WHA-JxOTZ'  # Mothix
# API_KEY = '3-8MeG-xlFh-ZlQgO'  # Matis

# Image par défaut si aucune image n'est trouvée
IMG_DEFAULT = "./assets/LEGO_logo.png"
# Télécharger les images des sets ou conserver les URL
DOWNLOAD_IMG = None
CATEGORIES = ['Normal', 'Book', 'Gear'] # Catégories de sets à afficher


###########################################################
# & Fonctions Utils
###########################################################


def init(api_key: str):
    """
    Initialiser l'API avec la clé donnée

    Args:
    - api_key (str): La clé d'API pour accéder à Brickset.
    """
    brickse.init(api_key)


def get_db_info() -> dict:
    """
    Récupérer les informations sur la base de données locale.

    Return:
    - dict: Informations sur la base de données (nombre de sets et de thèmes).
    """
    path = 'data/sets.json'
    path = os.path.join(os.path.dirname(__file__), path)

    sets = utils.load_sets_from_file(path)

    path = 'data/themes.json'
    path = os.path.join(os.path.dirname(__file__), path)
    themes = utils.load_themes_from_file(path)

    fromyear = min(theme['yearFrom'] for theme in themes)
    toyear = max(theme['yearTo'] for theme in themes)

    return {
        "nbSets": len(sets),
        "nbThemes": len(themes),
        "minyear": fromyear,
        "maxyear": toyear
    }


def get_all_set_from_api(theme: str) -> list[dict]:
    """
    Récupérer tous les sets d'un thème depuis l'API. (limité à 500 sets par page)

    Args:
    - theme (str): Le thème des sets à récupérer.

    Return:
    - list[dict]: Liste des sets du thème.
    """
    liste_sets = []
    nb_sets = 0

    for key_api in API_KEY:
        init(key_api)
        try:
            # obtenir le nombre de sets
            filename = 'themes.json'
            path_script = os.path.dirname(__file__)
            path_file = os.path.join(path_script, init_data.FICHIER)
            path_data = os.path.join(path_file, filename)
            liste_themes = utils.load_sets_from_file(path_data)
            for theme_item in liste_themes:
                if theme_item['theme'] == theme:
                    nb_sets = theme_item['setCount']

            for i in range(1, nb_sets // 500 + 2):
                set_500 = json.loads(brickse.lego.get_sets(
                    theme=theme, page_size=500, page=i).read())['sets']
                liste_sets.extend(set_500)
            return liste_sets
        except KeyError:
            if key_api == API_KEY[-1]:
                print("Nombre de requêtes dépassé pour toutes les clés API")
                return []
            print("Nombre de requêtes dépassé, changement de clé API")

    return liste_sets


def recherche_complete(liste, requete, limite=5, score_min=60):
    """
    Recherche les thèmes en utilisant d'abord une recherche par sous-chaîne,
    puis une recherche fuzzy si nécessaire.

    Args:
    - liste (list[str]): Liste des thèmes à rechercher.
    - requete (str): La requête de recherche.
    - limite (int): Le nombre maximum de résultats à retourner.
    - score_min (int): Le score minimum pour les correspondances fuzzy.

    Return:
    - list[str]: Liste des thèmes correspondant à la requête.
    """
    # Recherche par sous-chaîne (case-insensitive)
    requete_lower = requete.lower()
    correspondances = [
        theme for theme in liste if requete_lower in theme.lower()]

    if correspondances:
        return correspondances

    # Recherche fuzzy si aucune correspondance par sous-chaîne
    correspondances_fuzzy = process.extract(
        requete, liste, scorer=fuzz.WRatio, limit=limite)
    return [match[0] for match in correspondances_fuzzy if match[1] >= score_min]


###########################################################
# & Fonctions pour obtenir des informations sur les thèmes
###########################################################


def get_themes_name(yearfrom: int = None, yearto: int = None, search: str = None) -> list[dict]:
    """
    Obtenir la liste des thèmes et leur image filtrée par année et requête de recherche optionnelle.

    Args:
    - yearfrom (int): L'année minimale des thèmes à retourner.
    - yearto (int): L'année maximale des thèmes à retourner.
    - search (str): Requête de recherche approximative pour les noms des thèmes.

    Return:
    - list[dict]: Liste des thèmes avec l'image d'un set aléatoire.
    """
    # Charger les données
    themes = utils.load_themes_from_file(os.path.join(
        os.path.dirname(__file__), 'data/themes.json'))

    sets = utils.load_sets_from_file(os.path.join(
        os.path.dirname(__file__), 'data/sets.json'))
    sets = [s for s in sets if s['category'] in CATEGORIES]

    # Définir les bornes par défaut
    yearfrom = yearfrom or 1949
    yearto = yearto or datetime.date.today().year + 1

    # Filtrer les thèmes selon les années
    filtered_themes = [
        theme for theme in themes if (yearfrom <= theme['yearFrom'] and theme['yearTo'] <= yearto)
    ]

    # Appliquer une recherche approximative sur les noms des thèmes
    if search and search != "null":
        result_recherche = recherche_complete(
            [theme['theme'] for theme in filtered_themes], requete=search)
        filtered_themes = [
            theme for theme in filtered_themes if theme['theme'] in result_recherche]

    filtered_themes = [
        theme for theme in filtered_themes if theme['setCount'] > 0]

    # Préparer les données finales
    final_list = []
    for theme in filtered_themes:
        # Filtrer les sets associés au thème
        theme_sets = [
            lego_set for lego_set in sets if lego_set['theme'] == theme['theme']
        ]
        # Ne garder que les sets avec des images
        theme_sets = [s for s in theme_sets if s.get('image')]

        # Choisir une image aléatoire ou utiliser l'image par défaut
        if theme_sets:
            random_set = random.choice(theme_sets)
            img = random_set['image']['imageURL']
            if DOWNLOAD_IMG:
                img = utils.download_images_to_file(
                    [random_set['image']['imageURL']], random_set['number'])
        else:
            img = IMG_DEFAULT

        # Ajouter les informations du thème
        final_list.append({
            "name": theme['theme'],
            "image": img,
            "totalSets": theme['setCount'],
            "yearFrom": theme['yearFrom'],
            "yearTo": theme['yearTo'],
        })

    return final_list


###########################################################
# & Fonctions pour obtenir des informations sur les sets
###########################################################

def get_sets(theme: str = None, year: int = None,
             all_sets: bool = False, search: str = None) -> list[dict]:
    """
    Retourne la liste des sets pour un thème donné, avec le nom, l'image, le prix et la note.

    Args:
    - theme (str): Le thème des sets à retourner.
    - year (int): L'année des sets à retourner.
    - all_sets (bool): Si True, retourne tous les sets, sinon filtre par thème et année.
    - search (str): Requête de recherche approximative pour les noms des sets.

    Return:
    - list[dict]: Liste des sets avec le nom, l'image, le prix et la note.
    """
    # Charger les données locales
    fichier = 'data/sets.json'
    local_sets = utils.load_sets_from_file(fichier)

    # Filtrer les sets normaux
    sets_normal = [s for s in local_sets if s['category'] in CATEGORIES]

    # Appliquer les filtres sauf si all_sets est True
    if not all_sets:
        if theme:
            liste_themes = [theme["name"] for theme in get_themes_name()]
            if theme in liste_themes:
                sets_normal = [s for s in sets_normal if s['theme'] == theme]
            else:
                return []
        if year:
            sets_normal = [s for s in sets_normal if s['year'] == year]

    # Appliquer une recherche approximative sur les noms des sets
    if search and search != "null":
        result_recherche = recherche_complete(
            [s['name'] for s in sets_normal], requete=search)
        sets_normal_filtré = [
            s for s in sets_normal if s['name'] in result_recherche]

        result_recherche = recherche_complete(
            [s['theme'] for s in sets_normal], requete=search)
        sets_normal_filtré.extend(
            [s for s in sets_normal if s['theme'] in result_recherche and s['name'] not in sets_normal])
        sets_normal = sets_normal_filtré

    # Vérifier si des données manquent
    if not sets_normal and not all_sets:  # Si aucune donnée filtrée n'est trouvée, effectuer un appel API
        print("Récupération des données depuis l'API...")
        api_sets = get_all_set_from_api(theme)
        # Ajouter les nouveaux sets aux données locales
        local_sets.extend(api_sets)
        # Mettre à jour le fichier local
        utils.save_sets_to_file(local_sets, fichier)
        sets_normal = [s for s in local_sets if s['category'] in CATEGORIES]
        sets_normal = [s for s in sets_normal if s['theme']
                       == theme] if theme else sets_normal
        sets_normal = [s for s in sets_normal if search.lower(
        ) in s['name'].lower()] if search else sets_normal
        print(len(sets_normal), "sets trouvés")

    # Retirer les sets avec un nom incorrect
    sets_normal = [s for s in sets_normal if s['name'] != "{?}"]

    # Construire la liste finale
    result = []
    for lego_set in sets_normal:
        if lego_set.get('image'):
            if DOWNLOAD_IMG:
                img = utils.download_images_to_file([lego_set['image']['imageURL']], lego_set['number'])
            else:
                img = lego_set['image']['imageURL']
        else:
            img = IMG_DEFAULT

        price = next(
            (price_info['retailPrice'] for price_info in lego_set.get(
                'LEGOCom', {}).values() if price_info and price_info.get('retailPrice')),
            None
        )

        result.append({
            "number": lego_set['number'],
            "name": lego_set['name'],
            "image": img,
            "price": price,
            "rating": lego_set.get('rating'),
            "year": lego_set.get('year'),
        })

    return result


def get_set_info(set_number: str) -> list[dict]:
    """
    Obtenir les informations sur un set

    Args:
    - set_number (int): Le numéro du set

    Return:
    - list[dict]: Liste des informations sur le set
    (nom, image, prix, note, thème, pièces, minifigurines, description, dernière mise à jour,
    dimensions, lien Lego)
    """
    # Lit les données locales
    sets = utils.load_sets_from_file('data/sets.json')

    # Trouver le set correspondant
    set_info = next((s for s in sets if s['number'] == set_number), None)
    if not set_info:
        return []

    # Pour chaque clé, vérifier si elle existe dans les données du set
    # Si non, ajouter la clé avec la valeur None pour éviter les erreurs
    data = ["number", "name", "image", "price", "rating", "theme",
            "pieces", "minifigs", "extendedData", "lastUpdated", "dimensions"]
    for key in data:
        if key not in set_info:
            set_info[key] = None
    if set_info['extendedData'] is not None:
        if 'description' not in set_info['extendedData']:
            set_info['extendedData']['description'] = None

    # Récupérer toutes les images du set en demandant à l'API les images supplémentaires
    if len(set_info['image']) > 0:
        img = [set_info['image']['imageURL']] if set_info.get(
            'image') else []
        # Récupérer les images supplémentaires
        list_dict_img = json.loads(brickse.lego.get_set_images(
            set_info['setID']).read())['additionalImages']
        for dict_img in list_dict_img:
            img.append(dict_img['imageURL'])
        if DOWNLOAD_IMG:
            img = utils.download_images_to_file(img, set_number)
    else:
        img = [IMG_DEFAULT]

    # Parcours tout les pays pour trouver le prix si il existe, None sinon
    price = next(
        (info['retailPrice']
         for info in set_info.get('LEGOCom', {}).values() if info),
        None
    )

    # Récupérer les dimensions du set, None si elles n'existent pas
    dimensions = set_info.get("dimensions", {})
    dimensions.setdefault("weight", None)
    dimensions.setdefault("height", None)
    dimensions.setdefault("width", None)
    dimensions.setdefault("depth", None)

    # Récupérer la description du set, None si elle n'existe pas
    description = set_info.get("extendedData", {}).get("description", None)

    # Lien Lego
    lego_link = f"https://www.lego.com/fr-fr/product/{set_number}"

    # Construire la réponse
    return [{
        "number": set_info.get("number"),
        "name": set_info.get("name"),
        "image": img,
        "price": price,
        "rating": set_info.get("rating"),
        "theme": set_info.get("theme"),
        "pieces": set_info.get("pieces"),
        "minifigs": set_info.get("minifigs"),
        "description": description,
        "lastUpdated": set_info.get("lastUpdated"),
        "dimensions": dimensions,
        "legoLink": lego_link
    }]


###########################################################
# & Initialisation
###########################################################

if __name__ == '__main__':
    init(API_KEY)
