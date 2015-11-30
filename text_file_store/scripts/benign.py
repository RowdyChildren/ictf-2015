# In this example, we use a (rather stupid) library to interact with the service
import sys
import re
import requests
import random
import string
# To create random strings
POSSIBILITIES = string.ascii_uppercase + string.digits + string.ascii_lowercase

def benign(ip, port):
   
   
    # There should be some other benign traffic to your service.
    # It helps determine if the service is functional or not, and makes it
    # harder to fingerprint flag-related traffic.
    #
    # In this case, I was lazy and I'm just creating a dummy note.

    
    content = ''.join(random.choice(POSSIBILITIES) for x in range(20))
    
    r = requests.post('http://' + ip + ':' + str(port) + '/uploadFile.php?text=' + content , data = {})

    # make sure the request was successful
    
    assert r.status_code == 200

    #response = urllib2.urlopen(r.url);
    username = re.search(r'Username: ([0-9a-f]+)', r.text).group(1)
    password = re.search(r'Password: ([0-9a-f]+)', r.text).group(1)
    
    
     r = requests.post('http://' + ip + ':' + str(port) + '/viewFile.php' + '?userName=' + username + '&userPassword=' + password , data = {
        })
        


    # make sure the request was successful
    assert r.status_code == 200
    
    if re.search(r'Invalid Username or Password', r.text):
        raise WrongUsernameOrPassword

    # And let's check that we can read it...
    assert read_note(ip, port, note_id, password) == content

    # ... but just with the right password (in normal operation)
    # Note that we interpret _any_ exception as a sign that the service is not behaving correctly.
    # In this case, the WrongPassword exception is in fact expected.
    try:
        read_note(ip, port, note_id, wrong_password)
        raise "WTF? Notes can be read with wrong passwords even without vulnerabilities?"
    except WrongPassword:
        # All is good! Let's not pass this exception to the checking code
        pass

    # Nothing to return, if we got here without exceptions we assume that everything worked :)
