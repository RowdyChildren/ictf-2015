import sys
import re
import requests
import urllib2


class WrongUsernameOrPassword(Exception):
    pass

def get_flag(ip, port, flag_id, token):
    username = flag_id
    password = token


    #conn = socket.create_connection(ip, port)
   
    
    r = requests.post('http://' + ip + ':' + str(port) + '/viewFile.php' + '?userName=' + flag_id + '&userPassword=' + token , data = {
        })
        


    # make sure the request was successful
    assert r.status_code == 200
    
    if re.search(r'Invalid Username or Password', r.text):
        raise WrongUsernameOrPassword
    flag = r.text;
    
    

    return { 'FLAG': str(flag) }

print get_flag('127.0.0.1', '8080', '4c90f9d3495b4541' ,'8b3ba0f9c735f4def1128cb58749e45e617b12a6')
