document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search');
    const fromInput = document.getElementById('fromInput');
    const toInput = document.getElementById('toInput');
    const fromSlider = document.getElementById('fromSlider');
    const toSlider = document.getElementById('toSlider');
    const searchButton = document.getElementById('searchButton');

    console.log("Test")
    // Fonction pour mettre à jour l'URL avec les paramètres de recherche
    function updateURL() {
        const searchTerm = searchInput.value;
        const fromYear = fromInput.value;
        const toYear = toInput.value;

        const params = new URLSearchParams();
        if (searchTerm) params.set('search', searchTerm);
        if (fromYear) params.set('min', fromYear);
        if (toYear) params.set('max', toYear);

        const newURL = `${window.location.pathname}?${params.toString()}`;
        searchButton.href = newURL;
    }

    // Événements pour les entrées de recherche et de filtre
    searchInput.addEventListener('input', () => {
        updateURL();
    });
    fromInput.addEventListener('input', () => {
        fromSlider.value = fromInput.value;
        updateURL();
    });
    toInput.addEventListener('input', () => {
        toSlider.value = toInput.value;
        updateURL();
    });
    fromSlider.addEventListener('input', () => {
        fromInput.value = fromSlider.value;
        updateURL();
    });
    toSlider.addEventListener('input', () => {
        toInput.value = toSlider.value;
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