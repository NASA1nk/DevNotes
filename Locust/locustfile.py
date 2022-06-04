import base64
import json
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
        # register，注册用户        
        # payload = {
        #     "username": "1",
        #     "password": "1",
        #     "email": "1",
        #     "firstName": "1",
        #     "lastName": "1"
        # }
        # resp = {"id":"629af6a5a8fd2e000105560c"}

        # HOT THIS WEEK展示信息
        catalogue = self.client.get("/catalogue").json()
        # 随机选择一个商品
        category_item = choice(catalogue)
        item_id = category_item["id"]

        # 指定请求路径
        # 进入首页index.html
        self.client.get("/")
        # 登录，请求头中通过Authorization传递用户名和密码
        string = ('{0}:{1}'.format('user', 'password').replace('\n', '').encode("utf-8"))
        base64string = base64.b64encode(string)
        # print(f"========================{string}===============================")
        self.client.get("/login", headers={"Authorization": "Basic {0}".format(str(base64string, 'utf-8'))})
        # 用户信息
        self.client.get("/customers")
        # 进入商品列表页
        self.client.get("/category.html")
        # 进入随机选择的商品详情页
        self.client.get("/detail.html?id={}".format(item_id))
        # 进入购物车
        self.client.get("/cart")
        # 清空购物车(删除购物车中全部物品)
        self.client.delete("/cart")
        # 添加商品到购物车
        self.client.post("/cart", json={"id": item_id, "quantity": 1})
        # 删除购物车某件物品，应该需要携带cookie
        # self.client.delete(f"/cart/{item_id}")
        # 购物车页面
        self.client.get("/basket.html")
        # 提交订单
        self.client.post("/orders")


class Web(HttpUser):
    # 定义固定的task_set，指定前面的任务类名称
    tasks = [WebTasks]
    # tasks = [WebTasks]
    # 设置运行过程中间隔时间
    wait_time = between(0.1, 0.3)

if __name__ == "__main__":
    string = ('{0}:{1}'.format('user', 'password').replace(
            '\n', '').encode("utf-8"))
    base64string = base64.b64encode(string)

    t = "Basic {0}".format(str(base64string, 'utf-8'))
    print(string,base64string,t)


    catalogue = [{"id":"03fef6ac-1896-4ce8-bd69-b798f85c6e0b","name":"Holy","description":"Socks fit for a Messiah. You too can experience walking in water with these special edition beauties. Each hole is lovingly proggled to leave smooth edges. The only sock approved by a higher power.","imageUrl":["/catalogue/images/holy_1.jpeg","/catalogue/images/holy_2.jpeg"],"price":99.99,"count":1,"tag":["magic","action"]},{"id":"3395a43e-2d88-40de-b95f-e00e1502085b","name":"Colourful","description":"proident occaecat irure et excepteur labore minim nisi amet irure","imageUrl":["/catalogue/images/colourful_socks.jpg","/catalogue/images/colourful_socks.jpg"],"price":18,"count":438,"tag":["blue","brown"]},{"id":"510a0d7e-8e83-4193-b483-e27e09ddc34d","name":"SuperSport XL","description":"Ready for action. Engineers: be ready to smash that next bug! Be ready, with these super-action-sport-masterpieces. This particular engineer was chased away from the office with a stick.","imageUrl":["/catalogue/images/puma_1.jpeg","/catalogue/images/puma_2.jpeg"],"price":15,"count":820,"tag":["black","sport","formal"]},{"id":"808a2de1-1aaa-4c25-a9b9-6612e8f29a38","name":"Crossed","description":"A mature sock, crossed, with an air of nonchalance.","imageUrl":["/catalogue/images/cross_1.jpeg","/catalogue/images/cross_2.jpeg"],"price":17.32,"count":738,"tag":["red","formal","blue","action"]},{"id":"819e1fbf-8b7e-4f6d-811f-693534916a8b","name":"Figueroa","description":"enim officia aliqua excepteur esse deserunt quis aliquip nostrud anim","imageUrl":["/catalogue/images/WAT.jpg","/catalogue/images/WAT2.jpg"],"price":14,"count":808,"tag":["formal","blue","green"]},{"id":"837ab141-399e-4c1f-9abc-bace40296bac","name":"Cat socks","description":"consequat amet cupidatat minim laborum tempor elit ex consequat in","imageUrl":["/catalogue/images/catsocks.jpg","/catalogue/images/catsocks2.jpg"],"price":15,"count":175,"tag":["green","brown","formal"]},{"id":"a0a4f044-b040-410d-8ead-4de0446aec7e","name":"Nerd leg","description":"For all those leg lovers out there. A perfect example of a swivel chair trained calf. Meticulously trained on a diet of sitting and Pina Coladas. Phwarr...","imageUrl":["/catalogue/images/bit_of_leg_1.jpeg","/catalogue/images/bit_of_leg_2.jpeg"],"price":7.99,"count":115,"tag":["skin","blue"]},{"id":"d3588630-ad8e-49df-bbd7-3167f7efb246","name":"YouTube.sock","description":"We were not paid to sell this sock. It's just a bit geeky.","imageUrl":["/catalogue/images/youtube_1.jpeg","/catalogue/images/youtube_2.jpeg"],"price":10.99,"count":801,"tag":["geek","formal"]},{"id":"zzz4f044-b040-410d-8ead-4de0446aec7e","name":"Classic","description":"Keep it simple.","imageUrl":["/catalogue/images/classic.jpg","/catalogue/images/classic2.jpg"],"price":12,"count":127,"tag":["green","brown"]}]
    category_item = choice(catalogue)
    print(category_item)