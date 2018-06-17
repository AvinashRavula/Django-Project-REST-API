# import threading
#
# import requests
# from rest_framework import status
# from rest_framework.utils import json
#
#
# def fetch(req, id):
#     result = req.get("http://127.0.0.1:8000/onlineapp/api/v1/colleges/%s" % id)
#     print(result.content)
#     return
#
# if __name__ == '__main__':
#     req = requests.session()
#     req.auth = ('avi', 'avi')
#     result = req.get("http://127.0.0.1:8000/onlineapp/api/v1/colleges/6/students/")
#     print(result.content)
#     my_threads = [0 for val in range(25)]
#     for id in range(25):
#         my_threads[id] = threading.Thread(target=fetch, args=(req, id))
#         my_threads[id].start()
#         # t.join()
#
#     for index in range(25):
#         my_threads[index].join()
