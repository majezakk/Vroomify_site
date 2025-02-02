document.addEventListener('DOMContentLoaded', function() {
  // Код для анимации секций при прокрутке
  const sections = document.querySelectorAll('section');
  const observerOptions = { threshold: 0.2 };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animationPlayState = 'running';
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  sections.forEach(section => {
    observer.observe(section);
  });

  // Инициализация Flatpickr для выбора даты с русской локализацией
  if (document.querySelector("#date")) {
    flatpickr("#date", {
      locale: "ru",           // Русская локализация
      dateFormat: "d/m/Y",      // Формат даты: день/месяц/год
      allowInput: true          // Разрешить ввод вручную
    });
  }

  // Инициализация Flatpickr для выбора времени в 24-часовом формате
  if (document.querySelector("#time")) {
    flatpickr("#time", {
      enableTime: true,         // Включить выбор времени
      noCalendar: true,         // Отключить календарь (только время)
      dateFormat: "H:i",        // Формат времени: часы:минуты (24-часовой формат)
      time_24hr: true,          // Использовать 24-часовой формат
      allowInput: true          // Разрешить ввод вручную
    });
  }
});
