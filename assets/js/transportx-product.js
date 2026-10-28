document.addEventListener('DOMContentLoaded', () => {
  const page = document.querySelector('.transportx-application-page');
  if (!page) return;
  const tabs = [...page.querySelectorAll('[data-scene]')];
  const panels = [...page.querySelectorAll('.transportx-scene')];
  const selectScene = index => {
    tabs.forEach((tab, i) => {
      tab.setAttribute('aria-selected', String(i === index));
      tab.tabIndex = i === index ? 0 : -1;
      panels[i].hidden = i !== index;
    });
  };
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => selectScene(index));
    tab.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next === undefined) return;
      event.preventDefault();
      selectScene(next);
      tabs[next].focus();
    });
  });
  selectScene(0);
  const dialog = page.querySelector('.transportx-image-dialog');
  page.querySelectorAll('[data-preview]').forEach(button => {
    button.addEventListener('click', () => {
      const image = dialog.querySelector('img');
      image.src = button.dataset.preview;
      image.alt = button.dataset.caption;
      dialog.querySelector('p').textContent = button.dataset.caption;
      dialog.showModal();
    });
  });
  dialog.querySelector('button').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {
    if (event.target === dialog) {
      const rect = dialog.getBoundingClientRect();
      if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
    }
  });
});
