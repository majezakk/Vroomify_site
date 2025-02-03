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
      allowInput: true            // Разрешить ввод вручную
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

    const toggles = document.querySelectorAll('.password-toggle');

    toggles.forEach(toggle => {
        toggle.addEventListener('click', function () {
            const targetId = this.getAttribute('data-target');
            const passwordField = document.getElementById(targetId);

            if (passwordField.type === 'password') {
                passwordField.type = 'text';
                this.classList.remove('fa-eye');
                this.classList.add('fa-eye-slash');  // 👁️ Закрытый глаз
            } else {
                passwordField.type = 'password';
                this.classList.remove('fa-eye-slash');
                this.classList.add('fa-eye');        // 👁️ Открытый глаз
            }
        });
    });

  // 🛡️ Валидация формы регистрации (проверка совпадения паролей)
  const registrationForm = document.getElementById('registration-form');
  if (registrationForm) {
    registrationForm.addEventListener('submit', function(e) {
      const password = document.getElementById('password').value;
      const confirmPassword = document.getElementById('confirm_password').value;

      if (password !== confirmPassword) {
        e.preventDefault();
        alert('Пароли не совпадают. Пожалуйста, попробуйте снова.');
      }
    });
  }
});
