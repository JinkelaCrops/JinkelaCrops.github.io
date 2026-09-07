(() => {
  'use strict';
  const root = document.documentElement;
  const languageButton = document.getElementById('language');
  const themeButton = document.getElementById('theme');
  let language = 'zh';
  function setTheme(theme) {
    root.dataset.theme = theme;
    themeButton.setAttribute('aria-pressed', String(theme === 'dark'));
    themeButton.setAttribute('aria-label', language === 'zh' ? (theme === 'dark' ? '切换浅色模式' : '切换深色模式') : (theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'));
  }
  try {const saved = localStorage.getItem('portfolio-theme');if (saved === 'dark' || saved === 'light') setTheme(saved);} catch (_) { /* Local files can disallow storage. */ }
  themeButton.addEventListener('click', () => {
    const next = root.dataset.theme === 'dark' ? 'light' : 'dark';setTheme(next);
    try {localStorage.setItem('portfolio-theme', next);} catch (_) {}
  });
  languageButton.addEventListener('click', () => {
    language = language === 'zh' ? 'en' : 'zh';root.lang = language === 'zh' ? 'zh-CN' : 'en';
    document.querySelectorAll('[data-zh][data-en]').forEach(el => { el.textContent = el.dataset[language]; });
    languageButton.textContent = language === 'zh' ? 'EN' : '中文';
    languageButton.setAttribute('aria-label', language === 'zh' ? 'Switch to English' : '切换为中文');
    setTheme(root.dataset.theme);
  });
})();
