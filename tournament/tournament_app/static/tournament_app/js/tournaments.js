function sortTournaments() {
    const container = document.getElementById('tournament-container');
    const cards = Array.from(container.getElementsByClassName('tournament-card'));
    const sortBy = document.getElementById('sort').value;

    cards.sort((a, b) => {
        let aValue, bValue;
        if (sortBy === 'date') {
            aValue = new Date(a.getAttribute('data-date'));
            bValue = new Date(b.getAttribute('data-date'));
        } else if (sortBy === 'name') {
            aValue = a.getAttribute('data-name').toLowerCase();
            bValue = b.getAttribute('data-name').toLowerCase();
        } else if (sortBy === 'host') {
            aValue = a.getAttribute('data-host').toLowerCase();
            bValue = b.getAttribute('data-host').toLowerCase();
        } else if (sortBy === 'gamemode') {
            aValue = a.getAttribute('data-gamemode').toLowerCase();
        }

        if (aValue < bValue) return -1;
        if (aValue > bValue) return 1;
        return 0;
    });

    cards.forEach(card => container.appendChild(card));
}

function searchTournaments() {
    const searchInput = document.getElementById('search').value.toLowerCase();
    const cards = document.querySelectorAll('.tournament-card');

    cards.forEach(card => {
        const name = card.getAttribute('data-name').toLowerCase();
        card.style.display = name.includes(searchInput) ? 'block' : 'none';
    });
}