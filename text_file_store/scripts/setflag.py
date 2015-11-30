import sys
import re
import requests
import urllib2
import string

def set_flag(ip, port, flag):
   
    r = requests.post('http://' + ip + ':' + str(port) + '/uploadFile.php?text=' + flag , data = {})

    # make sure the request was successful
    
    assert r.status_code == 200

    #response = urllib2.urlopen(r.url);
    username = re.search(r'Username: ([0-9a-f]+)', r.text).group(1)
    password = re.search(r'Password: ([0-9a-f]+)', r.text).group(1)
    
    return {
        'FLAG_ID': str(username),
        'TOKEN': str(password),  # benign (get_flag) will know this, exploits will not
            }


