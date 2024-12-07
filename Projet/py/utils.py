# -*- coding: utf-8 -*-
"""
Ce module fournit des fonctions utilitaires pour gérer les sets Lego, y compris
la sauvegarde et le chargement des sets depuis un fichier JSON local.

Fonctions:
- save_sets_to_file(sets: list[dict], file_path: str):
    Enregistre les sets dans un fichier JSON local.

- load_sets_from_file(file_path: str) -> list[dict]:
    Charge les sets depuis un fichier JSON local.
"""
import os
import json
import requests


def save_sets_to_file(sets: list[dict], file_path: str):
    """
    Enregistre les sets dans un fichier JSON local.

    Args:
    - sets: list[dict] - Les sets à enregistrer.
    - file_path: str - Le chemin du fichier JSON.
    """
    path_script = os.path.dirname(__file__)
    path_data = os.path.join(path_script, file_path)
    with open(path_data, 'w', encoding='utf-8') as file:
        json.dump(sets, file, ensure_ascii=False, indent=4)


def load_sets_from_file(file_path: str) -> list[dict]:
    """
    Charge les sets depuis un fichier JSON local.

    Args:
    - file_path: str - Le chemin du fichier JSON.

    Returns:
    - list[dict]: Les sets chargés depuis le fichier JSON.
    """
    try:
        path_script = os.path.dirname(__file__)
        path_data = os.path.join(path_script, file_path)
        with open(path_data, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def load_themes_from_file(file_path: str) -> list[dict]:
    """
    Charge les thèmes depuis un fichier JSON local.

    Args:
    - file_path: str - Le chemin du fichier JSON.

    Returns:
    - list[dict]: Les thèmes chargés depuis le fichier JSON.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def download_images_to_file(url: list[str], set_num: str) -> list[str]:
    """
    Télécharge une liste d'images depuis une URL et les enregistre dans un fichier.

    Args:
    - url: str - L'URL de l'image à télécharger.
    - file_path: str - Le chemin du fichier dans lequel enregistrer l'image.

    Returns:
    - str: Le chemin relatif de l'image enregistrée.
    """
    fichier = '../assets/sets/'
    path = os.path.join(os.path.dirname(__file__), fichier, set_num)

    # Créer le dossier s'il n'existe pas
    if not os.path.exists(path):
        os.makedirs(path)

    # Télécharger les images
    for i, lien in enumerate(url):
        file_path = os.path.join(path, lien.split('/')[-1])
        if not os.path.exists(file_path):
            print(f'Téléchargement de l\'image {lien.split("/")[-1]} - {set_num} ({i+1}/{len(url)})')
            response = requests.get(lien, stream=True, timeout=50) # Télécharger l'image
            with open(file_path, 'wb') as file:
                file.write(response.content)

    return [f'{fichier[1:]}{set_num}/{lien.split("/")[-1]}' for lien in url]
