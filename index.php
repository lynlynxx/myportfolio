<!DOCTYPE html>
<html lang="en">
<head>>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registrer & Login</title>
    <link rel="stylesheet" href="0">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container" id="signin">
        <h1 class="form-title">Sign In</h1>
        <form method="post" action="login.php">
            <div class="input-group">
                <i class="fas fa-envelope"></i>
                <input type="email" name="email" id="email" placeholder>
                <label for="email">Email</label>
            </div>
            <div class="input-group">
                <i class="fas-fa-lock"></i>
                <input type="password" name="password" id="password">
                <label for="password">Password</label>
            <div>
            <p class="recover">
                <a href="#">Recover Password</a>
            <p>
        <input type="submit" class="btn" value="Sign in" name="signin">
    </form>
</div> 

</body>   
</html>            