(() => {
  const navButton = document.querySelector('[data-menu-trigger]');
  const mobileNav = document.querySelector('[data-mobile-nav]');
  const closeMenu = () => {
    if (!navButton || !mobileNav) return;
    navButton.setAttribute('aria-expanded', 'false');
    mobileNav.classList.remove('open');
    document.body.classList.remove('no-scroll');
  };
  if (navButton && mobileNav) {
    navButton.addEventListener('click', () => {
      const open = navButton.getAttribute('aria-expanded') !== 'true';
      navButton.setAttribute('aria-expanded', String(open));
      mobileNav.classList.toggle('open', open);
    });
    mobileNav.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
    document.addEventListener('keydown', e => { if (e.key === 'Escape') closeMenu(); });
    document.addEventListener('click', e => {
      if (!mobileNav.contains(e.target) && !navButton.contains(e.target)) closeMenu();
    });
  }

  const search = document.querySelector('[data-menu-search]');
  const categoryButtons = Array.from(document.querySelectorAll('[data-filter]'));
  const items = Array.from(document.querySelectorAll('[data-menu-item]'));
  const sections = Array.from(document.querySelectorAll('[data-menu-section]'));
  const count = document.querySelector('[data-menu-count]');
  const empty = document.querySelector('[data-menu-empty]');
  const korean = document.documentElement.lang === 'ko';
  let filter = 'all';
  const applyFilter = () => {
    const query = (search?.value || '').normalize('NFKC').trim().toLocaleLowerCase();
    let visible = 0;
    for (const item of items) {
      const matchesCategory = filter === 'all' || item.dataset.category === filter;
      const matchesQuery = !query || (item.dataset.menuItem || '').normalize('NFKC').toLocaleLowerCase().includes(query);
      item.hidden = !(matchesCategory && matchesQuery);
      if (!item.hidden) visible++;
    }
    for (const section of sections) {
      section.hidden = !section.querySelector('[data-menu-item]:not([hidden])');
    }
    if (count) count.textContent = korean ? `${visible}개 메뉴 표시` : `Showing ${visible} dishes`;
    if (empty) empty.hidden = visible !== 0;
  };
  if (search) search.addEventListener('input', applyFilter);
  categoryButtons.forEach(button => button.addEventListener('click', () => {
    filter = button.dataset.filter;
    categoryButtons.forEach(other => {
      const active = other === button;
      other.classList.toggle('active', active);
      other.setAttribute('aria-pressed', String(active));
    });
    applyFilter();
  }));
  if (items.length) applyFilter();

  const dialog = document.querySelector('[data-lightbox]');
  if (dialog && typeof dialog.showModal === 'function') {
    const lightboxImage = dialog.querySelector('img');
    document.querySelectorAll('[data-open-image]').forEach(button => {
      button.addEventListener('click', () => {
        lightboxImage.src = button.dataset.openImage;
        lightboxImage.alt = button.dataset.imageAlt || '';
        dialog.showModal();
      });
    });
    dialog.querySelector('[data-lightbox-close]')?.addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', e => {
      const rect = dialog.getBoundingClientRect();
      if (e.clientX < rect.left || e.clientX > rect.right || e.clientY < rect.top || e.clientY > rect.bottom) dialog.close();
    });
  }

  const reveals = Array.from(document.querySelectorAll('.reveal'));
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08 });
    reveals.forEach(el => observer.observe(el));
  } else {
    reveals.forEach(el => el.classList.add('visible'));
  }
})();
