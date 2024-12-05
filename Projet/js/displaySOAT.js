async function displaySetDetails() {
    const set = (await getSetById())[0]; // Accéder au premier élément de l'array
    if (set) {
        // Mettre à jour les détails du set
        document.getElementById('header-title').textContent = set.name || 'Nom non disponible';

        document.getElementById('header-subtitle').innerHTML = set.theme || 'Thème non disponible';
        document.getElementById('header-subtitle').href = `./sets.html?theme=${encodeURIComponent(set.theme)}`;
        document.getElementById('header-subtitle').textContent = set.theme || 'Thème non disponible';

        document.getElementById('details-description').innerHTML = set.description || 'Description non disponible';
        document.getElementById('features-list').innerHTML = `
            <tbody class="bg-gray-800 divide-y divide-gray-700">
                <tr>
                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-white">Nombre</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">#${set.number}</td>
                </tr>
                <tr>
                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-white">Pièces</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">${set.pieces !== null ? set.pieces : 'Prix non disponible'}</td>
                </tr>
                <tr>
                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-white">Minifigs</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">${set.minifigs !== null ? set.minifigs : 'Aucune minifigurine'}</td>
                </tr>
                <tr>
                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-white">Prix</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">${set.price !== null ? set.price + ' €' : 'Prix non disponible'}</td>
                </tr>
                <tr>
                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-white">Évaluation</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">${set.rating}/5</td>
                </tr>
                <tr>
                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-white">Dimensions</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">
                        ${set.dimensions.height || set.dimensions.width || set.dimensions.depth
                ? `${set.dimensions.height ?? "?"}cm x ${set.dimensions.width ?? "?"}cm x ${set.dimensions.depth ?? "?"}cm`
                : "Dimension indisponible"}
                    </td>
                </tr>
                <tr>
                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-white">Poids</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">${set.dimensions.weight !== null ? set.dimensions.weight + ' kg' : 'Poids non disponible'}</td>
                </tr>
            </tbody>
    `;

        const imageSection = document.getElementById('image-section');
        const imageGrid = document.createElement('div');
        const numImages = set.image.length;

        let numCols = Math.ceil(Math.sqrt(numImages));
        imageGrid.className = `grid grid-cols-${numCols} gap-4 w-full h-full`;

        set.image.forEach((imageUrl, index) => {
            const imageDiv = document.createElement('div');
            imageDiv.className = 'w-full h-full';
            const img = document.createElement('img');
            img.className = 'object-cover w-full h-full rounded-lg';
            img.src = imageUrl;
            img.alt = `Image ${index + 1}`;
            imageDiv.appendChild(img);

            // Si il y a un nombre impair d'images, la première image prendra 2 colonnes
            if (index === 0 && numImages % numCols !== 0) {
                imageDiv.classList.add('col-span-2');
            }

            imageGrid.appendChild(imageDiv);
        });

        imageSection.innerHTML = '';
        imageSection.appendChild(imageGrid);

        document.getElementById('cta-button').onclick = function () { window.open(set.legoLink, '_blank') };
    }
}

document.addEventListener('DOMContentLoaded', displaySetDetails);