document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.getElementById('productsCarousel');
    const prevBtn = document.getElementById('productsPrev');
    const nextBtn = document.getElementById('productsNext');

    if (!carousel || !prevBtn || !nextBtn) return;

    const scrollAmount = 260;

    prevBtn.addEventListener('click', () => {
        carousel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    });

    nextBtn.addEventListener('click', () => {
        carousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    });
});
