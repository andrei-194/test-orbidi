from fastapi import APIRouter
from fastapi import status
from fastapi.encoders import jsonable_encoder

from application.api_calls.api_calls import ApiCallApp
from application.hubspot.hubspot import HubspotApp
from models.user import User
from share.logging.logging import Logs

user_router = APIRouter()


@user_router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    logging = Logs()
    api_call_app = ApiCallApp()
    hubspot_app = HubspotApp()

    user_dict = user.to_dict()
    try:
        logging.log.warning("Inicia llamado endpoint")

        response = hubspot_app.create(user_dict)

        api_call_app.create_api_call(endpoint="/user", params=user_dict, result=f"{response}")
        logging.log.warning("Termina llamado endpoint")

        return jsonable_encoder({"status": f"{response}"})

    except Exception as e:
        api_call_app.create_api_call(endpoint="/user", params=user_dict, result=f"Error")
        return e
