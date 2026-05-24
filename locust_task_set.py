from locust import HttpUser, between, task, SequentialTaskSet



class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task(4)
    def get_home(self):
        self.client.get("/home")

    @task(1)
    def get_dashboard(self):
        self.client.get("/dashboard")







# # example
# class MyTaskSet(TaskSet):
#
#     @task
#     def task_one(self):
#         return self.client.get("/page1")
#
#     @task
#     def task_two(self):
#         return self.client.get("/page2")

# class MyTaskSet(SequentialTaskSet):
#
#     @task
#     def task_one(self):
#         return self.client.get("/page1")
#
#     @task
#     def task_two(self):
#         return self.client.get("/page2")
#
#     @task
#     def task_three(self):
#         return self.client.get("/page3")