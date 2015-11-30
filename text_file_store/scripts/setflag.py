import sys
import re
import requests
import urllib2

def set_flag(ip, port, flag):
    url = 'http://' + ip + ':' + str(port) + '/uploadFile.php'
    r = requests.post(url, data = {'text': flag})

    # make sure the request was successful
    assert r.status_code == 200

    response = urllib2.urlopen(r.url);
    for line in response
        if 'Username' in line
            u = line.split(':')
            username = u[1]
        else if 'Password' in line
            p = line.split(':')
            password = p[1]

if __name__ == "__main__":
    print set_flag(None, None, "FLG_just_testing")
