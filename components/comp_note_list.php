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
                <a class="navbar-brand" href="../index.php"> MyNote </a>
            </div>
        </div>
    </nav>


<?php  if (isset($_SESSION['username'])) : ?>        

    <?php

        global $db;
        $sql = "SELECT id, note_body, created_at FROM user_notes WHERE username_id = '".$_SESSION['username']."'";
        $result = mysqli_query($db, $sql);
        $rows = mysqli_num_rows($result);
        $html = "";

        if ($rows > 0) {
            while ($row = mysqli_fetch_assoc($result)) {
                $str = $row['note_body'];
                $str = str_replace(' ', '', $str);                                
                $note_name = (strlen($str) > 10) ? substr($row['note_body'],0,15).'...' : $row['note_body'];
                if ($note_name == "") {
                    $note_name = "Unamed note";
                }
                $html .= "<a href='./user_note.php?note_id=".$row['id']."'>";
                $html .= "<button class='media col-sm-4 col-lg-3 col-xl-4 mb-xl-1 overview__single black-border'>";
                $html .= "<div class='media-body'>";
                $html .= "<h3>".$note_name."</h3>";
                $html .= "<p>".$row['created_at']."</p>";
                $html .= "</button>";
                $html .= "</div>";
                $html .= "</a>";
            }
        } else {
            $html .= "<h2 class='section-intro__title' style='font-size: 23px; margin-left: 20%;'> No notes found </h2>";
        }
        echo $html;
    ?>

    <form method="post" action="../api/new_note.php">
        <div class="form-group col-sm-4 col-lg-3 col-xl-4 mb-2 mb-xl-0 b">
            <button type="submit" name="new_note" class="btn btn-success btn-circle btn-xl" style="font-size: 5em; border: 2px solid black">
                <i>+</i>
            </button>
        </div>
    </form>


<? else: ?>
    <?php
        header("Location:http://localhost/web_fin_proj/api/login.php"); 
        exit;
    ?>

<?php endif ?>
   


</body>
</html>