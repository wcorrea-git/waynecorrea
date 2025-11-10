// =====================================================
// SMOOTH SCROLLING & NAVIGATION
// =====================================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// =====================================================
// SCROLL ANIMATIONS
// =====================================================

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe achievement cards, expertise categories, and timeline items
document.querySelectorAll('.achievement-card, .expertise-category, .timeline-content').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
    observer.observe(el);
});

// =====================================================
// STATS COUNTER ANIMATION
// =====================================================

function animateCounters() {
    const stats = document.querySelectorAll('.stat-number');

    stats.forEach(stat => {
        const originalText = stat.textContent;

        // Extract the numeric value with decimal support
        const numberMatch = originalText.match(/[\d.]+/);
        const target = numberMatch ? parseFloat(numberMatch[0]) : 0;

        // Extract the suffix (B, M, %, +)
        const suffix = originalText.replace(/[\d$.]/g, '');
        const hasDollar = originalText.includes('$');

        const increment = target / 30;
        let current = 0;

        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }

            // Format output
            let display = current.toFixed(suffix === 'B' ? 1 : 0);
            if (hasDollar) display = '$' + display;
            display += suffix;
            stat.textContent = display;

            if (current >= target) clearInterval(timer);
        }, 50);
    });
}

// Trigger counter animation when hero section comes into view
const heroSection = document.querySelector('.hero');
const heroObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateCounters();
            heroObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

if (heroSection) {
    heroObserver.observe(heroSection);
}

// =====================================================
// NAVBAR SCROLL EFFECT
// =====================================================

const navbar = document.querySelector('.navbar');
let lastScrollPosition = 0;

window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;

    if (scrollPosition > lastScrollPosition && scrollPosition > 100) {
        // Scrolling down
        navbar.style.boxShadow = 'var(--shadow-md)';
    } else {
        // Scrolling up
        navbar.style.boxShadow = 'var(--shadow-sm)';
    }

    lastScrollPosition = scrollPosition;
});

// =====================================================
// PARALLAX EFFECT (Optional - Subtle)
// =====================================================

window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const circle = document.querySelector('.gradient-circle');

    if (circle) {
        circle.style.transform = `translateY(${scrolled * 0.5}px)`;
    }
});

// =====================================================
// ACTIVE NAV LINK HIGHLIGHTING
// =====================================================

window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');

    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').slice(1) === current) {
            link.classList.add('active');
        }
    });
});

// =====================================================
// MOBILE MENU (If added in future)
// =====================================================

// Add mobile menu toggle when needed
function initMobileMenu() {
    const navMenu = document.querySelector('.nav-menu');

    // Close menu when link is clicked
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
        });
    });
}

// =====================================================
// PAGE LOAD ANIMATION
// =====================================================

window.addEventListener('load', () => {
    document.body.style.opacity = '1';
});

// Initial state
document.body.style.opacity = '0.99';
document.body.style.transition = 'opacity 0.5s ease-out';

// =====================================================
// CONSOLE MESSAGE
// =====================================================

console.log('%cWayne Correa - Cloud Infrastructure Product Leader', 'font-size: 16px; font-weight: bold; color: #0066ff;');
console.log('%cBuilding the future of enterprise cloud connectivity', 'font-size: 12px; color: #64748b;');
console.log('%cContact: email@waynecorrea.com | LinkedIn: linkedin.com/in/waynecorrea', 'font-size: 11px; color: #94a3b8;');
