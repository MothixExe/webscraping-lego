async function displayDBInfo() {
    const info = await getDBInfo();

    document.getElementById('lego-sets').innerHTML = `${info.nbSets} sets LEGO`;
    document.getElementById('total-sets').innerHTML = info.nbSets;
    document.getElementById('total-themes').innerHTML = info.nbThemes;
    document.getElementById('oldest-year').innerHTML = info.minyear;
    document.getElementById('newest-year').innerHTML = info.maxyear;

    console.log(info);

}

document.addEventListener('DOMContentLoaded', displayDBInfo);