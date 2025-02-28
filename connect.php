<?php

$host="loacalhost";
$user="root";
$pass="";
$db="login";
$conn=new mysqli($host,$user,$pass,$db);
if($conn->connect_error){
    echo "Failed to conncet".$conn->connect_error;
}
?>