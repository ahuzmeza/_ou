<?php if (isset($_SESSION['username'])) : 

    $usr = $_SESSION['username']; 
    $note_id = $_GET['note_id'];

    $_SESSION['note_id'] = $note_id;

    $sql_get = "SELECT note_body
                FROM user_notes 
                WHERE id = '$note_id';";
    $content = mysqli_query($db, $sql_get);
    $result = mysqli_fetch_array($content);
    $note_body = $result['note_body'];
    // gets what was previously in the DB 
    // for the body of the note
?>

    <a class="btn delete-note my-2 my-sm-0" href="../api/delete_note.php">
    Delete note 
    </a>

    <form class="note" method="get" action="index.php" name="note_form" id="form">
        
        <textarea class="note__body" type="text" id="noteBody"> 
            <?php echo ($note_body); ?>
        </textarea>
        
    </form>

<?php endif ?>

<!-- Script to save text entered after <MILISECONDS> -->
<script>

// Get the input box
var textInput = document.getElementById('noteBody');
var timeout = null;

// Listen for keystrokes
textInput.onkeyup = function (e) {

    // Clear the timeout if it has already been set.
    // preventing the previous task from executing
    clearTimeout(timeout);
    // Make a new timeout set to go off in 800ms
    timeout = setTimeout ( 
        function () 
        {
            var txt = $("#noteBody").val();
              $.ajax({
                url:"../api/save_note.php?data="+txt,
                type: 'GET',
                data: {noteBody: txt },
                success: 
                function(data) {
                    console.log('Input Value:', txt);
                    // logs it
                        // changes color of background to visualize savestate
                        var el = document.getElementById('form');
                        var original = el.style.color;
                        el.style.backgroundColor='#004d1a';
                        window.setTimeout(function() { 
                                el.style.backgroundColor = original; 
                        }, 600); 
                } // endl color function
              }); // end ajax
            
        }, 600); // save timer 
    
}; // endscript


</script>