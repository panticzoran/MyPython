# Sending a GET request to JSONPlaceholder to retrieve a list of posts and then prints the different contents of the posts

import requests

def fetchPostTitle(postIndex):
    response = requests.get('https://jsonplaceholder.typicode.com/posts') # JSONPlaceholder = fake online REST API for testing and prototyping
    posts = response.json()  # Convert the response to a Python list

    if posts:
        return posts[postIndex]['title']
    else:
        return "No posts found."

def fetchPostBody(postIndex):
    response = requests.get('https://jsonplaceholder.typicode.com/posts') # JSONPlaceholder = fake online REST API for testing and prototyping
    posts = response.json()  # Convert the response to a Python list
    return posts[postIndex]['body']

for i in range(0,100):
    print("Title of the post #" + str(i) + ": " + fetchPostTitle(i))
    print("Body of the post #" + str(i) + ": " + fetchPostBody(i))
    print("\n")