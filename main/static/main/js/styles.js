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

  // Инициализация Flatpickr для выбора даты с правильным форматом
  if (document.querySelector("#date")) {
    flatpickr("#date", {
      locale: "ru",               // Русская локализация
      dateFormat: "Y-m-d",        // Формат даты для Django: год-месяц-день
      allowInput: true             // Разрешить ввод вручную
    });
  }

  // Инициализация Flatpickr для выбора времени в 24-часовом формате
  if (document.querySelector("#time")) {
    flatpickr("#time", {
      enableTime: true,           // Включить выбор времени
      noCalendar: true,           // Отключить календарь (только время)
      dateFormat: "H:i",          // Формат времени: часы:минуты (24-часовой формат)
      time_24hr: true,            // Использовать 24-часовой формат
      allowInput: true            // Разрешить ввод вручную
    });
  }

  // Обработка формы записи на услугу с помощью AJAX
  const appointmentForm = document.querySelector('#appointment form');
  if (appointmentForm) {
    appointmentForm.addEventListener('submit', function(event) {
      event.preventDefault();

      const formData = new FormData(appointmentForm);

      fetch(appointmentForm.action, {
        method: 'POST',
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        },
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        const messageContainer = document.createElement('div');
        messageContainer.className = data.success ? 'alert alert-success' : 'alert alert-danger';
        messageContainer.textContent = data.success ? data.message : 'Ошибка: ' + Object.values(data.errors).join(', ');

        appointmentForm.prepend(messageContainer);

        if (data.success) {
          appointmentForm.reset();
        }

        setTimeout(() => messageContainer.remove(), 5000); // Удалить сообщение через 5 секунд
      })
      .catch(error => console.error('Ошибка:', error));
    });
  }
});
