<?php

    include ("server.php");

    $usr = $_SESSION['username']; 

    $body = $_GET['data'];
    $sql_put = "UPDATE users
                SET body = '$body'
                WHERE username = '$usr' ;";
    mysqli_query($db, $sql_put);

// places new saved note body in DB
?>