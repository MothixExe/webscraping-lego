# -*- coding: utf-8 -*-
"""
Ce module démarre le serveur Flask et installe les modules nécessaires.
"""
import os
import webbrowser

import install_requirements as ir
import app_main as am
import init_data as data

if __name__ == '__main__':
    # Installer les modules requis
    ir.main()

    # Initialiser les données
    data.main()

    # Ouvrir le navigateur sur la page d'accueil
    if os.getcwd().split('\\')[-1] != 'py':
        os.chdir(os.getcwd() + '/py')
    path = os.path.join(os.path.dirname(os.getcwd()), 'index.html')
    webbrowser.open(path)

    # Démarrer le serveur Flask
    # os.system('flask --app app_main run')
    am.start_app()
