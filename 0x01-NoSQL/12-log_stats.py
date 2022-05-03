#!/usr/bin/env python3
"""
12. Log stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    nginx_collection = client.logs.nginx

    logs = nginx_collection.count_documents({})
    print(f"{logs} logs")

    get = nginx_collection.count_documents({"method": {"$in": ["GET"]}})
    post = nginx_collection.count_documents({"method": {"$in": ["POST"]}})
    put = nginx_collection.count_documents({"method": {"$in": ["PUT"]}})
    patch = nginx_collection.count_documents({"method": {"$in": ["PATCH"]}})
    delete = nginx_collection.count_documents({"method": {"$in": ["DELETE"]}})
    print(f"""Methods:
    \tmethod GET: {get}
    \tmethod POST: {post}
    \tmethod PUT: {put}
    \tmethod PATCH: {patch}
    \tmethod DELETE: {delete}""")

    get_status_check = nginx_collection.count_documents({
        "method": {"$in": ["GET"]},
        "path": {"$in": ["/status"]}
        })
    print(f"{get_status_check} status check")
