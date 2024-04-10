# Simple web request to a public REST API

import requests


# Testing to see if the "get" fetches the wole document
def testPosts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(response.json())

# Traversing through the fetched data, printing
def printPosts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        for post in posts[:5]:  # Printing the first 5 posts
            print(f"Post ID: {post['id']}, Title: {post['title']}, Body: {post['body']}")

testPosts()

print("\n")

printPosts()