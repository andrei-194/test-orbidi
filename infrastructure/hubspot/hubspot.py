from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInput
from hubspot.crm.contacts.exceptions import ApiException

api_client = HubSpot(access_token='your_access_token')


class HubspotHttp:
    def __init__(self):
        self.conn = HubSpot(access_token="pat-na1-bfa3f0c0-426b-4f0e-b514-89b20832c96a")

    def create_user(self, user):
        try:
            simple_public_object_input = SimplePublicObjectInput(
                properties=user
            )
            self.conn.crm.contacts.basic_api.create(
                simple_public_object_input=simple_public_object_input
            )

            return "OK"

        except ApiException as e:
            raise ApiException(
                status=e.status,
                reason=e.reason
            )

    def get_all_user(self):
        try:
            return self.conn.crm.contacts.get_all()

        except ApiException as e:
            raise ApiException(
                status=e.status,
                reason=e.reason
            )
