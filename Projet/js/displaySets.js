async function displaySets() {
    const urlParams = new URLSearchParams(window.location.search);
    const setsList = document.getElementById('setslist');
    const isLoading = document.getElementById('isLoading');
    const titre = document.getElementById('titre');
    const soustitre = document.getElementById('soustitre');
    const searchInput = document.getElementById('search');
    isLoading.style.display = 'flex';

    if (urlParams.has('search')) {
        const search = urlParams.get('search');
        searchInput.value = search;
        const sets = await searchSets();
        setsList.innerHTML = ''; // Vider la liste des thèmes avant d'ajouter les résultats de la recherche

        if (sets.length === 0) {
            setsList.innerHTML = '<h1 class="col-span-4 text-center text-3xl w-full font-bold text-red-500 mt-5">Aucun set ne correspond à votre recherche</h1>';
            titre.innerHTML = `Aucun set LEGO ne correspond à "${search}"`;
            soustitre.remove();
        } else {
            sets.forEach(set => {
                const setElement = document.createElement('a');
                setElement.href = `./SOAT.html?id=${encodeURIComponent(set.number)}`;
                setElement.className = "bg-red-500 rounded-lg shadow-lg overflow-hidden transform transition-transform duration-300 hover:scale-102 cursor-pointer";

                setElement.innerHTML = `
                    <div class="overflow-hidden">
                        <img src="${set.image}" alt="${set.name}" class="w-full h-48 object-cover transition-transform duration-300 hover:scale-110">
                    </div>
                    <div class="p-4 bg-red-500 border-t-4 border-black">
                        <h2 class="text-xl font-bold text-white title-card">${set.name}</h2>
                    </div>
                `;
                setsList.appendChild(setElement);
                console.log("Element ajouté : ", set);
                console.log("Nomber of sets: ", sets.length);
            });
            titre.innerHTML = `Sets LEGO correspondant à "${search}" - ${sets.length} sets`;
        }
    } else {
        // Sinon, afficher tous les sets
        const sets = await getAllSets();

        if (sets.length === 0) {
            setsList.innerHTML = '<h1 class="col-span-4 text-center text-3xl w-full font-bold text-red-500 mt-5">Aucun set LEGO n\'a été trouvé</h1>';
            titre.innerHTML = `Aucun set LEGO n'a été trouvé`;
            soustitre.innerHTML = `Essayez d'explorer les thèmes pour remplir la base de données en cliquant <a href="./theme.html" class="text-blue-500 hover:underline">ici</a>`;
        } else {
            sets.forEach(set => {
                const setElement = document.createElement('a');
                setElement.href = `SOAT.html?id=${encodeURIComponent(set.number)}`;
                setElement.className = "bg-red-500 rounded-lg shadow-lg overflow-hidden transform transition-transform duration-300 hover:scale-102 cursor-pointer";

                setElement.innerHTML = `
                <div class="overflow-hidden">
                    <img src="${set.image}" alt="${set.name}" class="w-full h-48 object-cover transition-transform duration-300 hover:scale-110">
                </div>
                <div class="p-4 bg-red-500 border-t-4 border-black">
                    <h2 class="text-xl font-bold text-white title-card">${set.name}</h2>
                </div>
            `;

                setsList.appendChild(setElement);
                console.log("Element ajouté : ", set);
                console.log("Nomber of sets: ", sets.length);
            });
            titre.innerHTML = `Liste de tous les sets LEGO - ${sets.length} sets`;
        }
        isLoading.style.display = 'none';
    }
}

document.addEventListener('DOMContentLoaded', displaySets);