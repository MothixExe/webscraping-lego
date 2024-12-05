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
import json


def save_sets_to_file(sets: list[dict], file_path: str):
    """
    Enregistre les sets dans un fichier JSON local.

    Args:
    - sets: list[dict] - Les sets à enregistrer.
    - file_path: str - Le chemin du fichier JSON.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
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
        with open(file_path, 'r', encoding='utf-8') as file:
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
