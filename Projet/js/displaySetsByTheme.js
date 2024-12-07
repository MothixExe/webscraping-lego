async function displayFilteredSets() {
    const setsList = document.getElementById('setslist');
    const isLoading = document.getElementById('isLoading');
    const urlParams = new URLSearchParams(window.location.search);
    const themeParam = urlParams.get('theme');
    const titre = document.getElementById('titre_theme');
    const titre_page = document.getElementById('titre_page');

    const nbofSets = document.getElementById('nombre_sets');
    const yearofshop = document.getElementById('annees_vente');
    const avgprice = document.getElementById('prix_moyen');

    var fromYear = 0;
    var toYear = 0;
    var sumprice = 0;
    var nbofsets = 0;

    isLoading.style.display = 'flex';

    if (themeParam) {
        titre.textContent = `${themeParam}`;
        titre_page.innerHTML = `Projet LEGO - ${themeParam}`;
    } else {
        titre.textContent = "Eheh t'es pas censé être là";
        titre_page.innerHTML = `Projet LEGO - Tricheur`;
    }

    setsList.innerHTML = '<h1 class="col-span-4 text-center w-full text-3xl font-bold text-blue-500 mt-5" id="chargement">Chargement et téléchargement des Sets ...</h1>';
    const titre_chargement = document.getElementById('chargement');

    const setsByTheme = await getSetsByTheme();


    setsByTheme.forEach(set => {
        const setElement = document.createElement('a');
        setElement.href = `./SOAT.html?id=${encodeURIComponent(set.number)}`;
        setElement.className = "bg-red-500 rounded-lg shadow-lg overflow-hidden transform transition-transform duration-300 hover:scale-102 cursor-pointer";

        const stars = generateStars(set.rating);

        setElement.innerHTML = `
            <div class="overflow-hidden">
                <img src="${set.image}" alt="${set.name}" class="w-full h-48 object-cover transition-transform duration-300 hover:scale-110">
            </div>
            <div class="p-4 bg-red-500 border-t-4 border-black h-1/3">
                <h2 class="text-xl font-bold text-white title-card">${set.name}</h2>
                <div class="mt-4 flex justify-between items-center">
                ${set.rating ? `
                    <div class="flex items-center text-2xl font-bold text-yellow-300 bg-black px-3 py-1 rounded-lg shadow-lg">
                        ${stars}
                        <p class="ms-1 text-lg font-medium text-yellow-300">${set.rating}</p>
                        <p class="ms-1 text-lg font-medium text-gray-500">sur</p>
                        <p class="ms-1 text-lg font-medium text-gray-500">5</p>
                    </div>`: ''}

                    ${set.price ? `<p class="text-2xl font-bold text-yellow-300 bg-black px-3 py-1 rounded-lg shadow-lg">${set.price} €</p>` : ''}
                </div>
            </div>
        `;

        setsList.appendChild(setElement);
        console.log("Element ajouté : ", set);

        if (set.year < fromYear || fromYear === 0) {
            fromYear = set.year;
        } else if (set.year > toYear || toYear === 0) {
            toYear = set.year;
        };

        if (set.price) {
            sumprice += set.price;
            nbofsets++;
        }
    });

    nbofSets.textContent = setsByTheme.length;

    if (fromYear === toYear) {
        yearofshop.textContent = `${fromYear}`;
    } else if (toYear === 0) {
        yearofshop.textContent = `Année non disponible`;
    } else {
        yearofshop.textContent = `${fromYear} - ${toYear}`;
    };

    if (nbofsets === 0) {
        avgprice.textContent = 'Moyenne non disponible';
    } else {
        avgprice.textContent = `${(sumprice / nbofsets).toFixed(2)} €`;
    };

    isLoading.style.display = 'none';
    titre_chargement.style.display = 'none';
}

function generateStars(rating) {
    const fullStar = '<svg class="w-4 h-4 text-yellow-300 me-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20"><path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/></svg>';
    const emptyStar = '<svg class="w-4 h-4 text-gray-300 me-1 dark:text-gray-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20"><path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/></svg>';

    let stars = '';
    for (let i = 0; i < 5; i++) {
        stars += i < rating ? fullStar : emptyStar;
    }
    return stars;
}

document.addEventListener('DOMContentLoaded', displayFilteredSets);