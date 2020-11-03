import requests

url = 'http://127.0.0.1:8000/show/api/'
headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFtYmlrYSIsImV4cCI6MTYwNDQwNDg1MSwiZW1haWwiOiJiYWNoaHVAZ21haWwuY29tIiwib3JpZ19pYXQiOjE2MDQ0MDE4NTF9.JaNQplRjZvQUwjs93IXHbI527s_q88wPW6Qgdu4DM9A'}
r = requests.get(url, headers=headers)
print('status code:',r.status_code,'\n','data:',r.text)