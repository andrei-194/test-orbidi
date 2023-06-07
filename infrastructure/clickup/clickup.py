import requests


class ClickUpHttp:

    def __init__(self):
        self.list_id = "900200532843"
        self.url = "https://api.clickup.com/api/v2/list/" + self.list_id + "/member"
        self.headers = {"Authorization": "pk_3182376_Q233NZDZ8AVULEGGCHLKG2HFXWD6MJLC"}

    def get_all_users(self):
        response = requests.get(self.url, headers=self.headers)
        return response.json()

