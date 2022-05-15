<?php include('server.php') ?>

<!DOCTYPE html>
<html lang="ro">

<head>
    <title> Atestat </title>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">

        <link rel="stylesheet" type="text/css" href="../css/style.css">
    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>

</head>
<body>

    <nav class="navbar navbar-inverse">
        <div class="container-fluid">
            <div class="navbar-header">
                <a class="navbar-brand" href="../index.php"> Back </a>
            </div>
        </div>
    </nav>
    
    <div class="modal-dialog modal-login">
    <div class="modal-content">
        <div class="modal-header">
                <div class="avatar">
                    <img src="../vendor/img/avatar.png">
                </div>
            <h4 class="modal-title"> Register </h4>
        </div>

            <br>
        <form method="post" action="register.php">
                <?php include('errors.php'); ?>
                <div class="form-group">
                    <input type="text" class="form-control" name="username" placeholder="Username" value="<?php echo $username; ?>">
                </div>
                <div class="form-group">
                    <input type="password" class="form-control" name="password_1" placeholder="Password">
                </div>
                <div class="form-group">
                    <input type="password" class="form-control" name="password_2" placeholder="Confirm Password">
                </div>
                <div class="form-group">
                    <button type="submit" class="btn" name="reg_user"> Register </button>
                </div>
                <a href="login.php">
                    <div class="modal-footer">
                        Already have an account?
                    </div>
                </a>

            </form>
        </div>
    </div>

</body>
</html>