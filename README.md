# signature
____
Установка<br><br>

- Клонирование репозитория
  + git clone https://github.com/DededGit/recognizer
  + cd signature
- Создание вирутального окружения
  + python -m venv venv
- Активация 
  + venv\Scripts\activate.bat
- Установка зависимостей
  + pip install -r requirements.txt
- Установка tesseract
  + https://github.com/UB-Mannheim/tesseract/wiki

Использование<br><br>

Перейти в папку с загрузкой и ввести:<br><br> python main.py

Проблемы возникщие при работе<br><br>
Если выдает ошибку что tesseract не установлен, добавьте C:\Program Files\Tesseract-OCR\ в PATH windows
