import json
import requests
import threading


json_data = 0

def get_posts(posts_url):
    global json_data
    json_data = requests.get(posts_url).json()


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/posts'
    t1 = threading.Thread(target=get_posts, args=(url,))
    t1.start()
    t1.join()
    with open("data.json", 'w') as f:
        json.dump(json_data, f)
