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

    get = nginx_collection.count_documents({"method": "GET"})
    post = nginx_collection.count_documents({"method": "POST"})
    put = nginx_collection.count_documents({"method": "PUT"})
    patch = nginx_collection.count_documents({"method": "PATCH"})
    delete = nginx_collection.count_documents({"method": "DELETE"})
    print(f"""Methods:
    \tmethod GET: {get}
    \tmethod POST: {post}
    \tmethod PUT: {put}
    \tmethod PATCH: {patch}
    \tmethod DELETE: {delete}""")

    get_status_check = nginx_collection.count_documents({
        "method": "GET",
        "path": "/status"
        })
    print(f"{get_status_check} status check")
