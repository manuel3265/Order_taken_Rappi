import logging, uvicorn
from time import strftime
from utils import logger, make_dirs
from routers.router_predict import router_predict
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, WebSocket, UploadFile, File


async_mode = None
make_dirs.Make('/var/log/order_taken/' + strftime('%Y-%m-%d')).make()
log = logger.Logger()
log.setup_logger('order_taken', strftime('/var/log/order_taken/' + strftime('%Y-%m-%d') + '/log-info.log'))

logging.getLogger().setLevel(int(20))
logger_order_taken = logging.getLogger('order_taken')

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_predict)
print('Running in the port: ' + str(8998))
uvicorn.run(app, host="0.0.0.0", port=90)


