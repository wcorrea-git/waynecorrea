document.addEventListener('DOMContentLoaded', function () {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const dropdowns = document.querySelectorAll('.main-nav .dropdown');
    const settingsToggle = document.querySelector('.settings-toggle');
    const settingsMenu = document.querySelector('.settings-menu');
    const themeSelect = document.getElementById('theme-select');

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
    }

    // Feather icons
    feather.replace();

    // Settings Dropdown & Theme Switcher
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
        if (currentTheme === 'dark') {
            document.body.classList.add('dark-mode');
            themeSelect.value = 'dark';
        }

        themeSelect.addEventListener('change', function () {
            if (this.value === 'dark') {
                document.body.classList.add('dark-mode');
                localStorage.setItem('theme', 'dark');
            } else {
                document.body.classList.remove('dark-mode');
                localStorage.setItem('theme', 'light');
            }
        });
    }

    // Close dropdowns when clicking outside
    document.addEventListener('click', function (e) {
        if (!e.target.closest('.main-nav')) {
            dropdowns.forEach(function (dropdown) {
                dropdown.classList.remove('is-open');
            });
        }
        const settingsDropdown = document.querySelector('.settings-dropdown');
        if (settingsDropdown && !settingsDropdown.contains(e.target)) {
            settingsDropdown.classList.remove('is-open');
        }
    });
});
