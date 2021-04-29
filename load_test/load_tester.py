import time
from locust import HttpUser, task, between
class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)
    @task
    def loading_page(self):
        self.client.get("loadhomepage")
    def sending_inputtext(self):
        self.client.post("inputtext", json={"book_hotel":"i would like to book a hotel"
                                            "book_car": "I would like to book a car"})
