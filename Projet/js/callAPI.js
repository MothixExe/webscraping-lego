const API_BASE_URL = 'http://localhost:5000';


async function getAllThemes() {
    console.log('Récupération de tous les thèmes ...');
    const response = await fetch(`${API_BASE_URL}/themes`);
    return await response.json();
}

async function getAllSets() {
    console.log('Récupération de tous les sets ...');
    const response = await fetch(`${API_BASE_URL}/all_sets`);
    return await response.json();
}

async function getSetsByTheme() {
    const urlParams = new URLSearchParams(window.location.search);
    const themeParam = urlParams.get('theme');
    if (themeParam) {
        console.log('Récupération des sets le thème : ' + themeParam + ' ...');
        const response = await fetch(`${API_BASE_URL}/theme/${themeParam}`);
        const data = await response.json();
        console.log(data);
        return data;
    } else {
        console.log('Aucun paramètre trouvé dans l\'URL');
        return [];
    }
}

async function getSetById() {
    const urlParams = new URLSearchParams(window.location.search);
    const setId = urlParams.get('id');
    if (setId) {
        console.log('Récupération du set avec l\'id : ' + setId + ' ...');
        const response = await fetch(`${API_BASE_URL}/set/${setId}`);
        const data = await response.json();
        console.log(data);
        return data;
    } else {
        console.log('Aucun paramètre trouvé dans l\'URL');
        return [];
    }
}

async function searchTheme() {
    const urlParams = new URLSearchParams(window.location.search);
    const search = urlParams.get('search');
    const min = urlParams.get('min');
    const max = urlParams.get('max');
    if (search || min || max) {
        console.log('Recherche du thème : ' + search + ' de l\'année ' + min + ' à l\'année ' + max + ' ...');
        const response = await fetch(`${API_BASE_URL}/theme/search/?yearFrom=${min}&yearTo=${max}&search=${search}`);
        const data = await response.json();
        console.log(data);
        return data;
    } else {
        console.log('Aucun paramètre trouvé dans l\'URL');
        return [];
    }
}

async function searchSets() {
    const urlParams = new URLSearchParams(window.location.search);
    const search = urlParams.get('search');
    if (search) {
        console.log('Recherche des sets avec le terme : ' + search + ' ...');
        const response = await fetch(`${API_BASE_URL}/all_sets/search/?search=${search}`);
        const data = await response.json();
        console.log(data);
        return data;
    } else {
        console.log('Aucun paramètre trouvé dans l\'URL');
        return [];
    }
}

async function getDBInfo() {
    console.log('Récupération des informations de la base de données ...');
    const response = await fetch(`${API_BASE_URL}/db_info`);
    return await response.json();
}