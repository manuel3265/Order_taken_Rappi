import json, random, time, shutil, logging, os, joblib
from pymongo import MongoClient
import pandas as pd
from fastapi import APIRouter, FastAPI, UploadFile, File, Request
from sklearn.preprocessing import MinMaxScaler
logger_order_taken = logging.getLogger('order_taken')
client = MongoClient(host='db', port=27017)
db=client.ordertaken
router_predict = APIRouter()
model = joblib.load('./pretrained/order_taken.pkl')
def error_function(error):
    response = {
        'status': 500,
        'error': error
    }
    return response

def normalize_scale(X):
  scaler = MinMaxScaler()
  scaler.fit(X)
  X_scaled = scaler.transform(X)
  return X_scaled

@router_predict.post('/predict')
async def stt_train(request: Request):
    collection = db.predictions
    columns = ["order_id", "store_id", "to_user_distance", "to_user_elevation", "total_earning", "created_at"]
    global df
    df = None
    try:
        data = await request.json()
        if isinstance(data, list):
            data_list = []
            for i in data:
                data_list.append([i["order_id"], i["store_id"], i["to_user_distance"], i["to_user_elevation"],
                                  i["total_earning"], i["created_at"]])
            df = pd.DataFrame(data_list, columns=columns)
        else:
            data_dict = {
                "order_id": [data["order_id"]],
                "store_id": [data["store_id"]],
                "to_user_distance": [data["to_user_distance"]],
                "to_user_elevation": [data["to_user_elevation"]],
                "total_earning": [data["total_earning"]],
                "created_at": [data["created_at"]]
            }
            df = pd.DataFrame.from_dict(data_dict)

        original_created_at = df['created_at']
        df['created_at'] = pd.to_datetime(df['created_at'], format='%Y-%m-%dT%H:%M:%SZ',
                                          errors='coerce').astype('datetime64').astype(int).astype(float)
        prediction = model.predict(normalize_scale(df.values))
        df['prediction'] = prediction
        df['created_at'] = original_created_at
        data_return = df.to_dict("records") if len(df) > 1 else df.to_dict("records")[0]
        if isinstance(data_return, list):
            for i in data_return:
                collection.insert_one(i)
                del i["_id"]
        else:
            collection.insert_one(data_return)
            del data_return["_id"]
        # logger_order_taken.info('Predictions: ' + data_return)

        # df_predict['created_at'] = pd.to_datetime(df_predict['created_at'], format='%Y-%m-%dT%H:%M:%SZ',
        #                                           errors='coerce').astype('datetime64').astype(int).astype(float)
        # df_predict = normalize_scale(df_predict)
        # logger_order_taken.info(df_predict)
        # predictions = model.predict(df_predict)

        return {
            'status': 200,
            'predictions': data_return
        }
    except Exception as e:
        logger_order_taken.error('An error occurred: ' + str(e))
        logger_order_taken.warning('Response: ' + str({'status': 0, 'data': "null"}))
        return error_function(str(e))



