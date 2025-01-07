from locust import task, HttpUser
import random


class PostsUser(HttpUser):
    """
    В вебинтерфейсе Locust указать этот хост: https://jsonplaceholder.typicode.com
    """
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    id_list = None
    response = None

    def on_start(self):
        """Создаю список с id постов, чтобы была возможность запрашивать случайный пост"""
        self.response = self.client.get('/posts', headers=self.headers)
        if self.response.status_code == 200:
            data = self.response.json()
            self.id_list = [item['id'] for item in data]
            print(self.id_list)
        else:
            print(f"Ошибка при получении списка постов, статус код: {self.response.status_code}")
            self.id_list = []

    @task(1)
    def get_random_post(self):
        if self.id_list:
            self.client.get(
                f'/posts/{random.choice(self.id_list)}',
                headers=self.headers
            )

    @task(3)
    def get_all_post(self):
        self.client.get('/posts', headers=self.headers)

    @task(2)
    def get_comments_random_post(self):
        if self.id_list:
            self.client.get(
                f'/comments?postId={random.choice(self.id_list)}',
                headers=self.headers
            )
