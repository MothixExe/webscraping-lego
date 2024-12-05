document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search');
    const searchButton = document.getElementById('searchButton');

    // Fonction pour mettre à jour l'URL avec les paramètres de recherche
    function updateURL() {
        const searchTerm = searchInput.value;

        const params = new URLSearchParams();
        if (searchTerm) params.set('search', searchTerm);

        const newURL = `${window.location.pathname}?${params.toString()}`;
        searchButton.href = newURL;
    }

    // Événements pour les entrées de recherche et de filtre
    searchInput.addEventListener('input', () => {
        updateURL();
    });

    // Événement pour le bouton rechercher
    searchButton.addEventListener('click', (event) => {
        event.preventDefault();
        updateURL();
        window.location.href = searchButton.href;
    });

    // Événement pour la touche "Entrée"
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            searchButton.click();
        }
    });
});