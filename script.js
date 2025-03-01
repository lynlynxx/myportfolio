document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll("section, .about-section, .projects-section, .contact-section, .hire-me-section");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("animate-section");
            }
        });
    }, { threshold: 0.3 });

    sections.forEach(section => {
        observer.observe(section);
    });

    document.querySelector(".menu-toggle").addEventListener("click", function() {
        document.querySelector(".menu").classList.toggle("active");
    });
    

});