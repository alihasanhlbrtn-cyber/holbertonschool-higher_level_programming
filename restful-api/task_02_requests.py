#!/usr/bin/python3
"""
Use the requests library to fetch posts from JSONPlaceholder,
print some info, and save posts to a CSV file.
"""

import requests
import csv


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():

    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    
    response = requests.get(API_URL)

    if response.status_code != 200:
        return  

    posts = response.json()


    data_to_save = [
        {
            "id": post.get("id"),
            "title": post.get("title"),
            "body": post.get("body"),
        }
        for post in posts
    ]


    with open("posts.csv", mode="w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["id", "title", "body"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data_to_save)

