document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.transportx-publication-archive').forEach((archive) => {
    const search = archive.querySelector('.filter-search');
    const filters = Array.from(archive.querySelectorAll('.pub-filters'));
    const entries = Array.from(archive.querySelectorAll('.transportx-publication-entry'));
    const emptyState = archive.querySelector('.transportx-publication-filter-empty');

    if (!search || entries.length === 0) return;

    const applyFilters = () => {
      const query = search.value.trim().toLocaleLowerCase();
      const activeClasses = filters
        .map((filter) => filter.value)
        .filter((value) => value !== '*')
        .map((value) => value.replace(/^\./, ''));
      let visibleCount = 0;

      entries.forEach((entry) => {
        const matchesQuery = !query || entry.textContent.toLocaleLowerCase().includes(query);
        const matchesFilters = activeClasses.every((className) => entry.classList.contains(className));
        const visible = matchesQuery && matchesFilters;

        entry.hidden = !visible;
        if (visible) visibleCount += 1;
      });

      if (emptyState) emptyState.hidden = visibleCount !== 0;
    };

    search.addEventListener('input', applyFilters);
    filters.forEach((filter) => filter.addEventListener('change', applyFilters));
  });
});
