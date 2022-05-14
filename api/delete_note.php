<?php

    include ("server.php");

    $note_id = $_SESSION['note_id'];
    $query = "DELETE FROM user_notes WHERE id = '$note_id'";
    mysqli_query($db, $query);
    
    // redirect to ../components/comp_note_list.php
    header("Location:../components/comp_note_list.php");
    exit;

?>