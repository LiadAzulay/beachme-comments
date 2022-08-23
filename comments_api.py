import pymongo
from fastapi import FastAPI
# Connecting to DB
mydb = pymongo.MongoClient('mongodb+srv://user:user@beachme.c5sbvhv.mongodb.net/?retryWrites=true&w=majority')["beachme-1"]
# Fetching "Comments"
comments_db = mydb.comments
# Creating api
app = FastAPI()


@app.get("/get_shore_comments/{id}")
async def root(id):
    comments = list(comments_db.find({"shore_id": int(id)}))
    for c in comments:
        c['_id'] = str(c['_id'])
    return comments

@app.get("/post_shore_comments/{shore_comment}")
async def root(shore_comment):
    return comments_db.insert_one(shore_comment)
