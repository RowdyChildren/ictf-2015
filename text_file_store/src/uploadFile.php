<?php
# This is your (only!) writeable directory. Store flags here.
$mydir = '/opt/ctf/text_file_store/rw/';
$text = $_POST['text'];
$userName = bin2hex(openssl_random_pseudo_bytes(8));
$userPassword = sha1(time() . '_' . $userName . '_' . bin2hex(openssl_random_pseudo_bytes(8)));
$filePart = base64_encode(sha1(sha1(sha1(sha1(sha1(sha1($userPassword)))))));
$fileName =  $fileName = $userName . '_' . $filePart;

$localFile = fopen($mydir.$fileName, "w") or die("Unable to open file!");
fwrite($localFile, $text);
fclose($localFile);
?>

<!DOCTYPE html>
<html>
<body>
    <p>Username: <?php echo $userName ?></p>
    <p>Password: <?php echo $userPassword ?></p>
    <p>Your data was stored and can be accessed <a href = "viewFile.php?file=<?php echo $fileName?>">here</a></p>
</body>
</html>
