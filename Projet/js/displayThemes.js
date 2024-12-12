async function displayThemes() {
    const themesList = document.getElementById('themeslist');
    const isLoading = document.getElementById('isLoading');
    const urlParams = new URLSearchParams(window.location.search);
    const fromInput = document.getElementById('fromInput');
    const toInput = document.getElementById('toInput');
    const fromSlider = document.getElementById('fromSlider');
    const toSlider = document.getElementById('toSlider');
    const searchInput = document.getElementById('search');

    // Si des paramètres sont présents dans l'URL, appeler searchTheme
    if (urlParams.has('search') || urlParams.has('min') || urlParams.has('max')) {
        const search = urlParams.get('search') || '';
        const min = urlParams.get('min') || fromInput.min;
        const max = urlParams.get('max') || toInput.max;

        // Remplir les valeurs des inputs et sliders avec les paramètres de l'URL
        searchInput.value = search;
        fromInput.value = min;
        toInput.value = max;
        fromSlider.value = min;
        toSlider.value = max;

        const themes = await searchTheme();
        themesList.innerHTML = ''; // Vider la liste des thèmes avant d'ajouter les résultats de la recherche

        if (themes.length === 0) {
            themesList.innerHTML = '<h1 class="col-span-4 text-center text-3xl w-full font-bold text-red-500 mt-5">Aucun thème ne correspond à votre recherche</h1>';
            isLoading.style.display = 'flex';
        } else {
            themes.forEach(theme => {
                const themeElement = document.createElement('a');
                themeElement.href = `./sets.html?theme=${encodeURIComponent(theme.name)}`;
                themeElement.className = "theme-element bg-red-500 rounded-lg shadow-lg overflow-hidden transform transition-transform duration-300 hover:scale-102 cursor-pointer flex flex-col";
            
                themeElement.innerHTML = `
                    <div class="flex flex-col h-full">
                        <div class="overflow-hidden flex-shrink-0">
                            <img src="${theme.image}" alt="${theme.name}" class="w-full h-48 object-cover transition-transform duration-300 hover:scale-110">
                        </div>
                        <div class="flex flex-col justify-between flex-grow p-4 bg-red-500 border-t-4 border-black">
                            <h2 class="text-xl font-bold text-white">${theme.name}</h2>
                            <div class="flex justify-between items-center mt-2">
                                <p class="text-xl font-bold text-yellow-300 bg-black px-3 py-1 rounded-lg shadow-lg">De ${theme.yearFrom} à ${theme.yearTo}</p>
                                <p class="text-xl font-bold text-yellow-300 bg-black px-3 py-1 rounded-lg shadow-lg">${theme.totalSets} sets</p>
                            </div>
                        </div>
                    </div>
                `;
            
                themesList.appendChild(themeElement);
            });
            
            
        }
    } else {
        // Sinon, afficher tous les thèmes
        themesList.innerHTML = '<h1 class="col-span-4 text-center w-full text-3xl font-bold text-blue-500 mt-5">Chargement des thèmes ...</h1>';
        isLoading.style.display = 'flex';
        const themes = await getAllThemes();

        // Trouver les années les plus basses et les plus hautes
        let minYear = Infinity;
        let maxYear = -Infinity;

        themes.forEach(theme => {
            if (theme.yearFrom < minYear) minYear = theme.yearFrom;
            if (theme.yearTo > maxYear) maxYear = theme.yearTo;
        });

        // Définir les valeurs des inputs et sliders
        fromInput.min = minYear;
        fromInput.max = maxYear;
        fromInput.value = minYear;

        toInput.min = minYear;
        toInput.max = maxYear;
        toInput.value = maxYear;

        fromSlider.min = minYear;
        fromSlider.max = maxYear;
        fromSlider.value = minYear;

        toSlider.min = minYear;
        toSlider.max = maxYear;
        toSlider.value = maxYear;

        themesList.innerHTML = ''; // Vider le message de chargement avant d'ajouter les thèmes
        isLoading.style.display = 'none';


        themes.forEach(theme => {
            const themeElement = document.createElement('a');
            themeElement.href = `./sets.html?theme=${encodeURIComponent(theme.name)}`;
            themeElement.className = "theme-element bg-red-500 rounded-lg shadow-lg overflow-hidden transform transition-transform duration-300 hover:scale-102 cursor-pointer flex flex-col";
        
            themeElement.innerHTML = `
                <div class="flex flex-col h-full">
                    <div class="overflow-hidden flex-shrink-0">
                        <img src="${theme.image}" alt="${theme.name}" class="w-full h-48 object-cover transition-transform duration-300 hover:scale-110">
                    </div>
                    <div class="flex flex-col justify-between flex-grow p-4 bg-red-500 border-t-4 border-black">
                        <h2 class="text-xl font-bold text-white">${theme.name}</h2>
                        <div class="flex justify-between items-center mt-2">
                            <p class="text-xl font-bold text-yellow-300 bg-black px-3 py-1 rounded-lg shadow-lg">De ${theme.yearFrom} à ${theme.yearTo}</p>
                            <p class="text-xl font-bold text-yellow-300 bg-black px-3 py-1 rounded-lg shadow-lg">${theme.totalSets} sets</p>
                        </div>
                    </div>
                </div>
            `;
        
            themesList.appendChild(themeElement);
        });
    }
}

document.addEventListener('DOMContentLoaded', displayThemes);