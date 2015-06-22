from locust import HttpLocust, TaskSet, task


class RestApiGetBehavior(TaskSet):

    @task()
    def get_rest_framework(self):
        self.client.get('http://localhost/rest_framework/entry/')

    @task()
    def get_django_views(self):
        self.client.get('http://localhost/django_view/entry/')

    @task()
    def get_tastypie(self):
        self.client.get('http://localhost/tastypie/entry/')

    @task()
    def get_restless(self):
        self.client.get('http://localhost/restless/entry/')

    @task()
    def get_nap(self):
        self.client.get('http://localhost/nap/api/entry/')


class GetApi(HttpLocust):
    task_set = RestApiGetBehavior


class RestApiPostBehavior(TaskSet):

    @task()
    def post_rest_framework(self):
        self.client.post('http://localhost/rest_framework/entry/',
                         {'title': 'hello', 'content': 'content', 'user': 'http://127.0.0.1/rest_framework/user/1/'})

    @task()
    def get_django_views(self):
        self.client.post('http://localhost/django_view/entry/',
                         {'title': 'hello', 'content': 'content', 'user': 'http://127.0.0.1/rest_framework/user/1/'})

    @task()
    def get_tastypie(self):
        self.client.post('http://localhost/tastypie/entry/',
                         {'title': 'hello', 'content': 'content', 'user': 'http://127.0.0.1/rest_framework/user/1/'})

    @task()
    def get_restless(self):
        self.client.post('http://localhost/restless/entry/',
                         {'title': 'hello', 'content': 'content', 'user': 'http://127.0.0.1/rest_framework/user/1/'})

    @task()
    def get_nap(self):
        self.client.post('http://localhost/nap/api/entry/',
                         {'title': 'hello', 'content': 'content', 'user': 'http://127.0.0.1/rest_framework/user/1/'})


class PostApi(HttpLocust):
    task_set = RestApiPostBehavior
