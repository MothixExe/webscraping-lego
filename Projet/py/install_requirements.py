# -*- coding: utf-8 -*-
"""
Ce code concerne l'installation des modules requis pour que l'application fonctionne.
Cela doit être exécuté avant de lancer l'application.
"""
import os
import subprocess
import sys


def install_missing_modules(modules):
    """
    Vérifier si les modules requis sont installés. Si ce n'est pas le cas, les installer.
    """
    choix = input("Voulez-vous installer les modules requis ? ([o]/n) : ")
    while choix.lower() not in ['o', 'n', '']:
        choix = input("Voulez-vous installer les modules requis ? ([o]/n) : ")
    if choix.lower() in ['o', '']:
        for module in modules:
            try:
                __import__(module)
            except ImportError:
                print(f"{module} n'est pas installé. Installation en cours...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", module])
                print(f"{module} installé avec succès.")
        print("Tous les modules requis sont installés.")


def main():
    """
    Installer les modules requis
    """
    if os.getcwd().split('\\')[-1] != 'py':
        os.chdir(os.getcwd() + '/py')
    with open('requirements.in', 'r', encoding='utf-8') as fichier:
        modules_requis = fichier.read().split('\n')
    modules_requis = [module.split("==")[0] for module in modules_requis if module]
    install_missing_modules(modules_requis)


if __name__ == '__main__':
    main()
