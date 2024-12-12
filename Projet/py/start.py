# -*- coding: utf-8 -*-
"""
Ce module démarre le serveur Flask et installe les modules nécessaires.
"""
import os
import webbrowser

import install_requirements as ir


if __name__ == '__main__':
    # Installer les modules requis
    ir.main()

    import init_data as data
    # Initialiser les données
    data.main()

    # Ouvrir le navigateur sur la page d'accueil
    path = os.path.join(os.path.dirname(__file__), '../index.html')
    webbrowser.open(path)

    # Démarrer le serveur Flask
    # os.system('flask --app app_main run')
    import app_main as am
    am.start_app()
