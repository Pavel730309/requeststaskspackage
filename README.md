# 📡 Python HTTP-запросы с библиотекой Requests

Репозиторий содержит решения практических заданий по теме **"Основы работы с библиотекой Requests"** из курса "Программист на Python с нуля".

---

## 📝 Задания

### ✅ Задание 1: Получение данных
- Отправка GET-запроса на [GitHub API](https://api.github.com/search/repositories)
- Поиск репозиториев по ключу `html`
- Вывод статус-кода и ответа в формате JSON

### ✅ Задание 2: Параметры запроса
- Использование API [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts)
- GET-запрос с параметром `userId=1`
- Вывод списка постов

### ✅ Задание 3: Отправка данных (POST)
- POST-запрос на `https://jsonplaceholder.typicode.com/posts`
- Отправка словаря: `{"title": "foo", "body": "bar", "userId": 1}`
- Вывод статус-кода и JSON-ответа

---

## 🚀 Как запустить

```bash
pip install requests
python requests_tasks.py
```

---

## 📁 Файлы

- `requests_tasks.py` — основной файл с выполненными заданиями
- `README.md` — описание проекта

---

## 💡 Автор

Задания выполнены в рамках практики по Python.  
Поддержка: [university.zerocoder.ru](https://university.zerocoder.ru)
