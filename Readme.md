# Order taken predictor

The database used is mongodb which is put in a container

## Pre - requisites

- Have docker installed
- Have docker-compose installed

### For mongo connection
- Have mongo installed

## Run the project

It is only necessary to execute the following line

```
docker-compose up --build -d
```

## Testing the project and the model

The project has a rest api exposed, which supports requests in the following ways

The endpoint is exposed in `HOST_IP:8998` with request type `POST`

### Endpoint

`http://HOST_IP:8998/predict`

### As simple prediction request 
```json
{

    "order_id": 14823213,
    "store_id": 900004658,
    "to_user_distance": 0.4203918115401082,
    "to_user_elevation": 14.37304687,
    "total_earning": 4500,
    "created_at": "2017-09-15T23:52:45Z"
}
```
### Or batch prediction request

```json
[
    {
    
        "order_id": 14823213,
        "store_id": 900004658,
        "to_user_distance": 0.4203918115401082,
        "to_user_elevation": 14.37304687,
        "total_earning": 4500,
        "created_at": "2017-09-15T23:52:45Z"
    },
    {
    
        "order_id": 15736509,
        "store_id": 900008202,
        "to_user_distance": 2.856551926076853,
        "to_user_elevation": 46.383911132812955,
        "total_earning": 5950,
        "created_at": "2017-10-01T18:00:05Z"
    }
]
```

### As simple prediction response 
```json
{
    "status": 200,
    "predictions": {
        "order_id": 14823213,
        "store_id": 900004658,
        "to_user_distance": 0.4203918115401082,
        "to_user_elevation": 14.37304687,
        "total_earning": 4500,
        "created_at": 1.505519565e+18,
        "prediction": 1
    }
}
```
### Or batch prediction response

```json
{
    "status": 200,
    "predictions": [
        {
            "order_id": 14823213,
            "store_id": 900004658,
            "to_user_distance": 0.4203918115401082,
            "to_user_elevation": 14.37304687,
            "total_earning": 4500,
            "created_at": 1.505519565e+18,
            "prediction": 1
        },
        {
            "order_id": 15736509,
            "store_id": 900008202,
            "to_user_distance": 2.856551926076853,
            "to_user_elevation": 46.383911132812955,
            "total_earning": 5950,
            "created_at": 1.506880805e+18,
            "prediction": 1
        }
    ]
}
```
# Connect to mongo
```console
mongo HOST_IP:9889/ordertaken
db.predictions.find({})
```
This will show the predictions that have been stored in the database

## Example
```console
mongo 34.70.225.254:9889/ordertaken
db.predictions.find({})
```

### Output
```console
{ "_id" : ObjectId("61058d78acfc6d734e661688"), "order_id" : 14823213, "store_id" : 900004658, "to_user_distance" : 0.4203918115401082, "to_user_elevation" : 14.37304687, "total_earning" : 4500, "created_at" : "2017-09-15T23:52:45Z", "prediction" : 1 }
{ "_id" : ObjectId("61058d78acfc6d734e661689"), "order_id" : 15736509, "store_id" : 900008202, "to_user_distance" : 2.856551926076853, "to_user_elevation" : 46.383911132812955, "total_earning" : 5950, "created_at" : "2017-10-01T18:00:05Z", "prediction" : 1 }
{ "_id" : ObjectId("61058daa99e46d40f1077643"), "order_id" : 14823213, "store_id" : 900004658, "to_user_distance" : 0.4203918115401082, "to_user_elevation" : 14.37304687, "total_earning" : 4500, "created_at" : "2017-09-15T23:52:45Z", "prediction" : 1 }
{ "_id" : ObjectId("61058daa99e46d40f1077644"), "order_id" : 15736509, "store_id" : 900008202, "to_user_distance" : 2.856551926076853, "to_user_elevation" : 46.383911132812955, "total_earning" : 5950, "created_at" : "2017-10-01T18:00:05Z", "prediction" : 1 }

```


