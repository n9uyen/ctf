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
