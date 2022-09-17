from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datetime

# Connecting to DB
mydb = MongoClient(
    'mongodb+srv://user:user@beachme.c5sbvhv.mongodb.net/?retryWrites=true&w=majority')["beachme-1"]
# Fetching "Comments"
comments_db = mydb.comments
# Creating api
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/get_shore_comments/{id}")
async def root(id):
    comments = list(comments_db.find({"shore_id": int(id)}))
    for c in comments:
        c['_id'] = str(c['_id'])
    return comments


@app.post("/post_shore_comments")
async def root(shore_comment: dict):
    shore_comment['timestamp'] = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    id = str(comments_db.insert_one(shore_comment))
    return id
    
