<?php

    include ("server.php");

    $usr = $_SESSION['username']; 
    $note_id = $_SESSION['note_id'];
    
    $body = $_GET['data'];
    $sql_put = "UPDATE user_notes
                SET note_body = '$body'
                WHERE id = '$note_id';";
    mysqli_query($db, $sql_put);


// places new saved note body in DB
?>