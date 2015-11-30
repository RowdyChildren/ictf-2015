<?php
$mydir = '/opt/ctf/text_file_store/rw/';
if (isset($_GET['file']))
{
    $fileName = $_GET['file'];
    if ((@include $mydir.$fileName) == TRUE) {
       //@include $mydir.$fileName;
    }
    else {
        echo "Invalid Username or Password";
    }
}
else
{
    $userPassword = $_GET['userPassword'];
    $fileName = $_GET['userName'] . '_' . base64_encode(sha1(sha1(sha1(sha1(sha1(sha1($userPassword)))))));
    if ((@include $mydir.$fileName) == TRUE) {
       //@include $mydir.$fileName;
    }
    else {
        echo "Invalid Username or Password";
    }
    
}
?>