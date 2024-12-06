# Projet de Collecte Automatisée de Données Web

## Description
Ce projet permet de collecter des données sur les ensembles Lego en utilisant le web scraping et des appels API. Il inclut des scripts pour sauvegarder et charger les données localement, ainsi qu'une interface web pour interagir avec les données.

## Structure des fichiers

### Fichiers Python
- `py/utils.py` : Fournit des fonctions utilitaires pour gérer les sets Lego, y compris la sauvegarde et le chargement des sets depuis un fichier JSON local.
  - `save_sets_to_file(sets: list[dict], file_path: str)` : Enregistre les sets dans un fichier JSON local.
  - `load_sets_from_file(file_path: str) -> list[dict]` : Charge les sets depuis un fichier JSON local.
  - `load_themes_from_file(file_path: str) -> list[dict]` : Charge les thèmes depuis un fichier JSON local.

- `py/app_main.py` : Contient les routes Flask pour interagir avec les ensembles Lego.
  - `/all_sets/search/` : Obtenir tous les ensembles Lego avec des filtres.
  - `/all_sets` : Obtenir tous les ensembles Lego.
  - `/set/<set_number>` : Obtenir des informations sur un ensemble Lego spécifique.
  - `/db_info` : Obtenir des informations sur la base de données actuelle.

- `py/start.py` : Démarre le serveur Flask et installe les modules nécessaires.
  - `ir.main()` : Installe les modules requis.
  - `data.main()` : Initialise les données.
  - `am.start_app()` : Démarre le serveur Flask.

- `py/install_requirements.py` : Installe les modules requis pour que l'application fonctionne.
  - `install_missing_modules(modules)` : Vérifie et installe les modules requis.
  - `main()` : Lit les modules requis depuis `requirements.in` et les installe.

- `py/init_data.py` : Initialise les données en obtenant la liste des thèmes et des ensembles à partir de l'API et en les enregistrant dans des fichiers.
  - `save_json_to_file(data, filename)` : Enregistre les données dans un fichier.
  - `init_themes(filename='themes')` : Obtient la liste des thèmes.
  - `init_sets(filename='sets')` : Obtient la liste des ensembles.
  - `main()` : Initialise les données.

- `py/api_interact.py` : Contient toutes les fonctions pour interagir avec l'API Brickse et répondre aux requêtes du serveur Flask.
  - `init(api_key: str)` : Initialise l'API avec la clé donnée.
  - `get_db_info() -> dict` : Récupère les informations sur la base de données locale.
  - `get_all_set_from_api(theme: str) -> list[dict]` : Récupère tous les sets d'un thème depuis l'API.
  - `recherche_complete(liste, requete, limite=5, score_min=60)` : Recherche les thèmes en utilisant une recherche par sous-chaîne et fuzzy.
  - `get_themes_name(yearfrom: int = None, yearto: int = None, search: str = None) -> list[dict]` : Obtient la liste des thèmes filtrée par année et requête de recherche.
  - `get_sets(theme: str = None, year: int = None, all_sets: bool = False, search: str = None) -> list[dict]` : Retourne la liste des sets pour un thème donné ou la liste de tout les sets dispo dans le base de données
  - `get_set_info(set_number: str) -> list[dict]` : Obtient les informations sur un set.


### Fichiers HTML
- `index.html` : Page principale de l'interface web. Contient une section d'attention pour informer l'utilisateur sur l'état initial de la base de données.
- `theme.html` : Page affichant les différents thèmes des sets Lego. Permet de rechercher et filtrer les thèmes.
- `info.html` : Page contenant des informations sur le projet, les statistiques de la base de données et les crédits.
- `allsets.html` : Page affichant tous les sets Lego disponibles. Permet de rechercher des sets spécifiques.
- `sets.html` : Page affichant les détails des sets d'un thème spécifique.
- `soat.html` : Page affichant les détails d'un set Lego spécifique. (Sets Of All Time ^^ )


### Fichiers JavaScript
- `js/style.js` : Contient des fonctions et des classes pour manipuler et afficher les données des ensembles Lego.
- `js/researchTheme.js` : Gère la recherche de thèmes Lego en fonction des critères de l'utilisateur.
- `js/displayThemes.js` : Affiche les thèmes Lego sur la page en fonction des critères de recherche.
- `js/displayDBInfo.js` : Affiche les informations de la base de données sur la page d'information.
- `js/researchSets.js` : Gère la recherche de sets Lego en fonction des critères de l'utilisateur.
- `js/loadingAnim.js` : Gère l'animation de chargement.
- `js/displaySOAT.js` : Affiche les détails d'un set Lego spécifique sur la page SOAT (Sets Of All Time).
- `js/displaySets.js` : Affiche les sets Lego sur la page en fonction des critères de recherche.
- `js/timeSlider.js` : Gère les sliders de sélection de période pour la recherche de thèmes.
- `js/callAPI.js` : Contient les fonctions pour interagir avec l'API et récupérer les données.
- `js/menu.js` : Gère le menu mobile de l'interface web.
- `js/displaySetsByTheme.js` : Affiche les sets Lego filtrés par thème sur la page.

## Instructions pour faire fonctionner le programme

### Prérequis
- Python 3.x
- Flask
- Une connexion internet si vous n'avez jamais lancer le programme
