document.addEventListener('DOMContentLoaded', function () {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const dropdowns = document.querySelectorAll('.main-nav .dropdown');

    // Toggle mobile menu
    if (navToggle) {
        navToggle.addEventListener('click', function () {
            navMenu.classList.toggle('is-active');
            const isExpanded = navMenu.classList.contains('is-active');
            navToggle.setAttribute('aria-expanded', isExpanded);
        });
    }

    // Handle dropdowns on mobile (tap to open)
    if (window.innerWidth <= 768) {
        dropdowns.forEach(function (dropdown) {
            const link = dropdown.querySelector('a');
            link.addEventListener('click', function (e) {
                // Allow navigation to top-level page like journal.html
                if (e.target.href && !dropdown.classList.contains('is-open')) {
                    // On first tap, open dropdown, prevent navigation
                    e.preventDefault();
                    // Close other open dropdowns
                    dropdowns.forEach(d => {
                        if (d !== dropdown) d.classList.remove('is-open');
                    });
                    dropdown.classList.add('is-open');
                } else if (!e.target.href) {
                     // if it's not a link, prevent default
                     e.preventDefault();
                }
            });
        });

        // Close dropdowns when clicking outside
        document.addEventListener('click', function (e) {
            if (!e.target.closest('.main-nav')) {
                dropdowns.forEach(function (dropdown) {
                    dropdown.classList.remove('is-open');
                });
            }
        });
    }

    // Feather icons
    feather.replace();
});
// Settings Dropdown, Theme Switcher, and Language Switcher
document.addEventListener('DOMContentLoaded', function () {
    const settingsToggle = document.querySelector('.settings-toggle');
    const settingsMenu = document.querySelector('.settings-menu');
    const themeSelect = document.getElementById('theme-select');
    const langSelect = document.getElementById('lang-select');

    if (settingsToggle) {
        settingsToggle.addEventListener('click', function (e) {
            e.stopPropagation();
            const settingsDropdown = document.querySelector('.settings-dropdown');
            settingsDropdown.classList.toggle('is-open');
        });
    }

    if (themeSelect) {
        // Check for saved theme in localStorage
        const currentTheme = localStorage.getItem('theme');
        if (currentTheme) {
            document.body.classList.remove('light-mode', 'dark-mode');
            if (currentTheme !== 'light') {
                document.body.classList.add(currentTheme);
            }
            themeSelect.value = currentTheme;
        }

        themeSelect.addEventListener('change', function () {
            const selectedTheme = themeSelect.value;
            document.body.classList.remove('light-mode', 'dark-mode');
            if (selectedTheme !== 'light') {
                document.body.classList.add(selectedTheme);
            }
            localStorage.setItem('theme', selectedTheme);
        });
    }

    if (langSelect) {
        langSelect.addEventListener('change', function () {
            const selectedLang = langSelect.value;
            // For now, we will just show an alert.
            // A full implementation would require a more complex setup with a library like i18next.
            alert('Language switched to: ' + selectedLang);
        });
    }

    // Close settings dropdown when clicking outside
    document.addEventListener('click', function (e) {
        const settingsDropdown = document.querySelector('.settings-dropdown');
        if (settingsDropdown && !settingsDropdown.contains(e.target)) {
            settingsDropdown.classList.remove('is-open');
        }
    });
});
