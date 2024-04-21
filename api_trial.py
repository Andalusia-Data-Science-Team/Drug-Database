import requests

data = {
    'Username': 'visn16',
    'Password': 'visn16'
}

r = requests.post('https://online.lexi.com/lco/action/login',
    data=data )
print(r)
print(r.content)
