# WannaGame Chamionship

## Web - Tunt Robot (170pts)

![Image](https://github.com/n9uyen/ctf/blob/master/wannagame_Championship_UIT/1.png)

Solve basic mathematical expression and get flag. :joy: :joy:

#### Idea

Get element of expression and use `eval()` in Python to solve it. :sunglasses:

This is a [script](https://github.com/n9uyen/ctf/blob/master/wannagame_Championship_UIT/script.py) to solve challenge.

```python
import requests
import re
import os
s = requests.Session()
url = "http://45.122.249.68:8098/challenge.php"

r = s.get(url).text
while 1:
    try:
        find = ''.join(re.findall('<h1><br>(.*)',r))
        get_element = ''.join(re.findall('[0-9\(\)\+\-\*\./\"]', find)[:-5]) # Get number expressions
        result = eval(get_element)
        data = {"result": result}
        r = s.post(url, data=data).text
        # print (r)
        if 'Your flag:' in r:
            print(r)
            break
    except:
        break
```

And get flag.

![Image](https://github.com/n9uyen/ctf/blob/master/wannagame_Championship_UIT/2.png)

## Web - No cookie for u (200pts)

__Source code__

```python

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, decode_token
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import threading
import jwt
import config

app = Flask(__name__)
 
app.config['JWT_SECRET_KEY'] = config.key
jwtmanager = JWTManager(app)
blacklist = set()
lock = threading.Lock()
 
def delete_expired_tokens():
    with lock:
        to_remove = set()
        global blacklist
        for access_token in blacklist:
            try:
                jwt.decode(access_token, app.config['JWT_SECRET_KEY'],algorithm='HS256')
            except:
                to_remove.add(access_token)
       
        blacklist = blacklist.difference(to_remove)
 
@app.route("/")
def index():
    src = open("app.py").read()
    return src
 
# Standard login endpoint
@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.json.get('username', None)
        password = request.json.get('password', None)
    except:
        return jsonify({"msg":"""{"username":"admin","password":"admin"}"""}), 400
 
    if username != 'admin' or password != 'admin':
        return jsonify({"msg": "Invalid"}), 401
 
    access_token = create_access_token(identity=username,expires_delta=datetime.timedelta(minutes=3))
    ret = {
        'access_token': access_token,
    }
   
    with lock:
        blacklist.add(access_token)
 
    return jsonify(ret), 200
 
# Standard admin endpoint
@app.route('/admin', methods=['GET'])
@jwt_required
def protected():
    access_token = request.headers.get("Authorization").split()[1]
    with lock:
        if access_token in blacklist:
            return jsonify({"msg":"403 Forbidden"})
        elif "ImlkZW50aXR5IjogIm5vdC1hZG1pbiI" not in access_token:
            return jsonify({"msg":"403 Forbidden"})
        else:
            return jsonify({'Flag': config.flag})
 
 
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    job = scheduler.add_job(delete_expired_tokens, 'interval', seconds=10)
    scheduler.start()
    app.run(debug=False, host='0.0.0.0', port=5000)

```
Read source code, have main routes: `login`, `admin`.

In `login` route, to create access token, login as admin use `POST` method with username and password: `admin:admin`, get access token in response.

![Image](https://github.com/n9uyen/ctf/blob/master/wannagame_Championship_UIT/3.png)

In `admin` route, to authenticate as admin, add `Authorization: Beaerer <token>` to request headers.

To get flag, `ImlkZW50aXR5IjogIm5vdC1hZG1pbiI` (`"identity": "not-admin"`) must in access_token.

#### Fact

I have tried some ways to bypass: brute-force weak signature, add `identity` in request but it's not working.

Fun fact, I try add "qwerty" to endpoint in access token.
Result:

![Image](https://github.com/n9uyen/ctf/blob/master/wannagame_Championship_UIT/4.png)

Wait a minute, token is valid. :thinking:

I add `ImlkZW50aXR5IjogIm5vdC1hZG1pbiI` to endpoint access token and get flag. ¯\\\_(ツ)\_/¯ 

![Image](https://github.com/n9uyen/ctf/blob/master/wannagame_Championship_UIT/5.png)

Flag is: `wannagame{488c5171c6ffc123b377acc6cf55e7c46bf06017}`

__Thanks for reading, sorry for my bad engrisk.__
