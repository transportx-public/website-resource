(() => {
  const photos = Array.from(document.querySelectorAll('[data-gallery-photo]'));
  const dialog = document.querySelector('#tx-gallery-dialog');
  if (!dialog || typeof dialog.showModal !== 'function') return;
  const image = dialog.querySelector('[data-gallery-preview]');
  const caption = dialog.querySelector('[data-gallery-caption]');
  let index = 0;
  function show(nextIndex) {
    index = (nextIndex + photos.length) % photos.length;
    image.src = photos[index].href;
    image.alt = photos[index].querySelector('img').alt;
    caption.textContent = `${index + 1} / ${photos.length}`;
  }
  photos.forEach((link, photoIndex) => link.addEventListener('click', event => {
    event.preventDefault();
    show(photoIndex);
    dialog.showModal();
  }));
  dialog.querySelector('.tx-gallery-close').addEventListener('click', () => dialog.close());
  dialog.querySelector('.tx-gallery-prev').addEventListener('click', () => show(index - 1));
  dialog.querySelector('.tx-gallery-next').addEventListener('click', () => show(index + 1));
  dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener('keydown', event => {
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault();
      show(index + (event.key === 'ArrowLeft' ? -1 : 1));
    }
  });
})();
