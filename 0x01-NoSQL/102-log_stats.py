#!/usr/bin/env python3
"""
15. Log stats - new version
"""


from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    nginx_collection = client.logs.nginx

    logs = nginx_collection.count_documents({})
    print(f"{logs} logs")

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

    top_ips = nginx_collection.aggregate([
        {'$group': {
            '_id': '$ip',
            'count': {'$sum': 1}
        }},
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ])
    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip.get('_id')}: {ip.get('count')}")
