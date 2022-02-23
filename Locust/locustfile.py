import base64
from random import choice
from locust import HttpUser, task, between, TaskSet
import locust.stats

# csv文件写入频率，默认1s
locust.stats.CSV_STATS_INTERVAL_SEC = 5
# 默认10s
locust.stats.CSV_STATS_FLUSH_INTERVAL_SEC = 5

# 定义用户行为
class WebTasks(TaskSet):

    # 一个任务
    @task
    def load(self):
        string = ('{0}:{1}'.format('user', 'password').replace('\n', '').encode("utf-8"))
        base64string = base64.b64encode(string)

        catalogue = self.client.get("/catalogue").json()
        category_item = choice(catalogue)
        item_id = category_item["id"]
        
        # 指定请求路径
        self.client.get("/")
        self.client.get("/login", headers={"Authorization": "Basic {0}".format(str(base64string, 'utf-8'))})
        self.client.get("/customers")
        self.client.get("/category.html")
        self.client.get("/detail.html?id={}".format(item_id))
        self.client.delete("/cart")
        self.client.post("/cart", json={"id": item_id, "quantity": 1})
        self.client.get("/basket.html")
        self.client.post("/orders")
        # self.client.get("/index.html")

class Web(HttpUser):
    # 定义固定的task_set，指定前面的任务类名称
    task_set = WebTasks
    # tasks = [WebTasks]
    # 设置运行过程中间隔时间
    wait_time = between(0.1, 0.3)
