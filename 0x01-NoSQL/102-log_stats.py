#!/usr/bin/env python3
"""102-log_stats.py"""
from pymongo import MongoClient

def top_students(mongo_collection):
    """
    Returns all students sorted by average score and the top 10 most present IPs in the "nginx" collection of the "logs" database.
    :param mongo_collection: pymongo collection object
    :return: List of students documents with average score and a list of the top 10 most present IPs
    """
    students_pipeline = [
        {"$unwind": "$scores"},
        {"$group": {"_id": "$_id", "averageScore": {"$avg": "$scores.score"}}},
        {"$sort": {"averageScore": -1}}
    ]
    students_cursor = mongo_collection.aggregate(students_pipeline)
    students_list = list(students_cursor)
    client = MongoClient()
    nginx_collection = client.logs.nginx
    ip_top_pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    ip_top_cursor = nginx_collection.aggregate(ip_top_pipeline)
    ip_top_list = list(ip_top_cursor)
    return (students_list, ip_top_list)
