# Задание 1: Получение данных с GitHub API
import requests
import pprint

print("Задание 1: GitHub API — поиск по 'html'")
url1 = "https://api.github.com/search/repositories"
params1 = {"q": "html"}
response1 = requests.get(url1, params=params1)
print(f"Статус-код: {response1.status_code}")
pprint.pprint(response1.json())

print("\n" + "="*80 + "\n")

# Задание 2: Параметры запроса — JSONPlaceholder
print("Задание 2: JSONPlaceholder — userId=1")
url2 = "https://jsonplaceholder.typicode.com/posts"
params2 = {"userId": 1}
response2 = requests.get(url2, params=params2)
print(f"Статус-код: {response2.status_code}")
pprint.pprint(response2.json())

print("\n" + "="*80 + "\n")

# Задание 3: Отправка данных (POST-запрос)
print("Задание 3: POST-запрос на JSONPlaceholder")
url3 = "https://jsonplaceholder.typicode.com/posts"
data3 = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
response3 = requests.post(url3, data=data3)
print(f"Статус-код: {response3.status_code}")
pprint.pprint(response3.json())
