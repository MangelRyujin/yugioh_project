const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting && entry.rootBounds.top + entry.rootBounds.height >= window.innerHeight * 0.7) {
            entry.target.classList.add('card-2-anima');
        } else {
            entry.target.classList.remove('card-2-anima');
        }
    });
}, {
    threshold: 0.1
});

document.querySelectorAll('.card-2').forEach(card => observer.observe(card));