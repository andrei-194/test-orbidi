from datetime import datetime

from infrastructure.db.db import DatabaseConnection
from models.api_calls.api_calls import ApiCall


class ApiCallApp:

    def __init__(self):
        self.conn = DatabaseConnection()

    def create_api_call(self, endpoint: str, params: dict, result: str):
        self.conn.connect()
        api_call = ApiCall(created_at=datetime.now(), endpoint=endpoint, params=params, result=result)
        self.conn.session.add(api_call)
        self.conn.session.commit()

    def get_all_api_calls(self):
        self.conn.connect()
        api_calls = self.conn.session.query(ApiCall).all()
        self.conn.disconnect()
        return api_calls
