import socket
import sys
import re
import requests
import urllib2

class WrongUsernameOrPassword(Exception)
    pass

def get_flag(ip, port, flag_id, token):
    username = flag_id
    password = token

    if ip:
        conn = socket.create_connection(ip, port)
        value = flag_id + '_' + token
        url = 'http://' + ip + ':' + str(port) + '/text_file_store/src/viewFile.php'
        r = requests.post(url, data = {'file': value})

    # make sure the request was successful
    assert r.status_code == 200

    if (re.search('Invalid Username or Password')
        raise WrongUsernameOrPassword
    flag = urllib2.urlopen(r.url).read();

    if ip: conn.close()

    return { 'FLAG': flag }

if __name__ == "__main__":
    print get_flag(None, None, sys.argv[1], sys.argv[2])
