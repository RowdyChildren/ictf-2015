import sys
import re
import requests
import urllib2

def set_flag(ip, port, flag):
   
    r = requests.post('http://' + ip + ':' + str(port) + '/text_file_store/src/uploadFile.php?text=' + flag , data = {})

    # make sure the request was successful
    
    assert r.status_code == 200

    #response = urllib2.urlopen(r.url);
    username = re.search(r'Username: ([0-9a-f]+)', r.text)
    password = re.search(r'Password: ([0-9a-f]+)', r.text)
    #for line in response:
    #    if 'Username' in line:
    #        u = line.split(': ')
    #        username = u[1]
    #        username.replace('</p>\\n', '')
    #    if 'Password' in line:
    #        p = line.split(': ')
    #        password = p[1]
    #        password.replace('</p>\\n', '')
    return {
        'FLAG_ID': username.group(1).replace('u\'', '\''),
        'TOKEN': password.group(1).replace('u\'', '\''),  # benign (get_flag) will know this, exploits will not
            }
            
print set_flag('127.0.0.1', '8080', 'test123')
