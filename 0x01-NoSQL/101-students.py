#!/usr/bin/env python3
"""101-students.py"""
def top_students(mongo_collection):
    
    """
    Returns all students sorted by average score.
    :param mongo_collection: pymongo collection object
    :return: List of students documents with average score
    """
    pipeline = [
        {"$unwind": "$scores"},
        {"$group": {"_id": "$_id", "averageScore": {"$avg": "$scores.score"}}},
        {"$sort": {"averageScore": -1}}
    ]
    cursor = mongo_collection.aggregate(pipeline)
    return list(cursor)
