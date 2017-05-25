dc = {100000: "python",
      100001: "java",
      100002: "nodejs"}
print(dc)

dc.update({"others": {100003: "javascript"}})
dc.update({100004: "sikuli"})

print('''
++++++++++++++
{}
'''.format(dc))

# coding:utf-8
from locust import HttpLocust, TaskSet, task
import queue


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        pass

    def index(self):
        self.client.get("/")

    @task
    def profile(self):
        with self.client.get(
                "/APIService/v2/enterprise/searchList?appkey=6c8e153ecd964671ac7ae5dc5d4b5e55&keyword=&#x5C0F;&#x7C73;&#x79D1;&#x6280;",
                catch_response=True) as resp:
            content = json.loads(resp.text)
            if (content['status'] == '200'):
                reps.success()
                print(resp.text)


class WebsiteUser(HttpLocust):
    host = "http://uatapi.qixin007.com"
    task_set = UserBehavior
    min_wait = 500
