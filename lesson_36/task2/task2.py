import json
import multiprocessing
from ctypes import c_char_p
import requests
from multiprocessing import Queue



def make_request(json_data, url_req):
    r = requests.get(url_req)
    json_data.put(r.json())


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = Queue()
    p = multiprocessing.Process(target=make_request, args=(data, url,))
    p.start()
    with open("data.json", 'w') as f:
        json.dump(data.get(), f)
    p.join()