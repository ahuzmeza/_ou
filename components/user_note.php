<!-- Main page -->
<?php include('../api/server.php') ?>

<!DOCTYPE html>
<html lang="ro">

<head>
    <title> MyNote - Service </title>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta author="ahuzmeza">
    
    <link rel="stylesheet" type="text/css" href="../css/style.css">
    
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>

</head>
<body>
<!-- ================ Menue =================-->
    <nav class="navbar navbar-inverse">
        <div class="container-fluid">
            <div class="navbar-header">
                <a class="navbar-brand" href="./comp_note_list.php"> MyNote </a>
            </div>
        </div>
    </nav>


 <?php include './comp_note.php'?>

 <script type="text/javascript" src="js/main.js"></script>
 
</body>
</html>