<?php

include 'connect.php';

if(isset($_POST['signin'])){
    $email=$_POST['email'];
    $password=$_POST['password'];
    $password=md5($password) ;

    $sql="SELECT * FROM users WHERE email='$email' and password='$password'"
    $result=$conn->query($sql);
    if($result->num_rows>0){
     seassion_start();
     $row=$result->fetch-assoc();
     $_SESSION['email']=$row['email'];
     header("Location: homepage.php");
     exit()
    }
}