<?php

    include ("server.php");

    if (isset($_POST['new_note'])) {
        $username = $_SESSION['username'];
        $query = "INSERT INTO user_notes (username_id, note_body) values ('$username', '')";
        mysqli_query($db, $query);
    }
    // redirect to ../components/comp_note_list.php
    header("Location:../components/comp_note_list.php");
    exit;

?>