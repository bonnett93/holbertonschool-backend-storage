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

    # get = nginx_collection.count_documents({"method": "GET"})
    # post = nginx_collection.count_documents({"method": "POST"})
    # put = nginx_collection.count_documents({"method": "PUT"})
    # patch = nginx_collection.count_documents({"method": "PATCH"})
    # delete = nginx_collection.count_documents({"method": "DELETE"})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    get_status_check = nginx_collection.count_documents({
        "method": "GET",
        "path": "/status"
        })
    print(f"{get_status_check} status check")
