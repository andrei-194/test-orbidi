from infrastructure.hubspot.hubspot import HubspotHttp


class HubspotApp:

    def __init__(self):
        self.hubspot_http = HubspotHttp()

    def create(self, user):
        self.hubspot_http.create_user(user)

    def get_all_user(self):
        self.hubspot_http.get_all_user()
