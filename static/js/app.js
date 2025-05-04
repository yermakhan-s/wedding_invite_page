// Fade in slides and content
const io = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('show');
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.15 });

document.querySelectorAll('.slide, [data-fade]').forEach(el => io.observe(el));

// Unmute music on first interaction
const bgm = document.getElementById('bgm');
const unlock = () => {
  bgm.muted = false;
  bgm.play().catch(() => {});
};
window.addEventListener('click', unlock, { once: true });
window.addEventListener('touchstart', unlock, { once: true });
