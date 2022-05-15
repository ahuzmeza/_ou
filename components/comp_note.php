<?php if (isset($_SESSION['username'])) : 

        $usr = $_SESSION['username']; 
    
        $sql_get = "SELECT body 
                    FROM users 
                    WHERE username = '$usr' ;";
        $content = mysqli_query($db, $sql_get);
        $result = mysqli_fetch_array($content);
        $body_inDb = $result['body'];
        // gets what was previously in the DB 
        // for the body of the note
        
/* ======================================== */     
?>
    
    <form class="note" method="get" action="index.php" name="note_form" id="form">

        <tittle class="note__title"> <?php echo $usr ?>'s note </tittle>
        
        <textarea class="note__body" type="text" id="noteBody"> 
            <?php echo ($body_inDb); ?>
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
                url:"api/save_note.php?data="+txt,
                type: 'GET',
                data: {noteBody: txt },
                success: 
                function(data) {
                    console.log('Input Value:', txt);
                    // logs it
                        // changes color of background to visualize savestate
                        var el = document.getElementById('form');
                        var original = el.style.color;
                        el.style.backgroundColor='#ccffcc';
                        window.setTimeout(function() { 
                                el.style.backgroundColor = original; 
                        }, 600); 
                } // endl color function
              }); // end ajax
            
        }, 600); // save timer 
    
}; // endscript
    
</script>