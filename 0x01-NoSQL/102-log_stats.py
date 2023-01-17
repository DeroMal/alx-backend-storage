#!/usr/bin/env python3
"""102-log_stats.py"""

def top_students(mongo_collection, nginx_collection):
    """
    Returns all students sorted by average score and the top 10 most present IPs in the "nginx" collection of the "logs" database.
    :param mongo_collection: pymongo collection object for students
    :param nginx_collection: pymongo collection object for nginx logs
    :return: List of students documents with average score and a list of the top 10 most present IPs
    """
    students_cursor = mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
    students_list = list(students_cursor)
    ip_top_cursor = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    ip_top_list = list(ip_top_cursor)
    return (students_list, ip_top_list)
