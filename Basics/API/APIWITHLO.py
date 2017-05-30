from locust import TaskSet,HttpLocust,task
import requests
import json

class A1Test(TaskSet):

    def on_start(self):
        self.data={"key1": "value1", "key2": "value2"}
        self.api='http://www.qichacha.com'
        self.headers = {"user-agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) \
                             Version/3.1 Safari/525.13"}

    def modify_parm(*args):
        def outer_deco(func):
            def wrapper(*args):
                data = self.data
                if(args==201):
                    data['key1']="value1"+'201'
                    func(data)
            return wrapper
        return outer_deco

    @task
    def test_get(self,data=self.data):
        with self.client.get(self.api,headers=self.headers,params=data,catch_response=True)   \
            as resp:
            # content=json.loads(resp.text)
            #            if (content['status'] == '200'):
            #                resp.success()
            print(resp.text)

    @task
    def test_return_code(self):
        test_get()


class TestA1Test(HttpLocust):
    host = ""
    task_set = A1Test
    min_wait = 500
