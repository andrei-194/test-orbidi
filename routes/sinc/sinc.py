from fastapi import APIRouter
from fastapi import status
from fastapi.encoders import jsonable_encoder

from application.api_calls.api_calls import ApiCallApp
from application.clickup.clickup import ClickUp
from share.logging.logging import Logs

sync_router = APIRouter()


@sync_router.get("/sync", status_code=status.HTTP_200_OK)
async def sync():
    logging = Logs()
    api_call_app = ApiCallApp()
    clickup_app = ClickUp()
    try:
        logging.log.warning("Inicia llamado endpoint")

        # api_call_app.create_api_call(endpoint="/sync", params={"method": "GET"}, result="OK")
        logging.log.warning("Termina llamado endpoint")
        return jsonable_encoder({"status": "OK"})

    except Exception as e:
        api_call_app.create_api_call(endpoint="/sync", params={"method": "GET"}, result=f"Error")
        return e
