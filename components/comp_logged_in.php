<!-- Username and Logour buttons appear when you ARE logged in -->
<li>
    <a href="#"><span class="glyphicon glyphicon-user"></span>
        &nbsp;
        <?php echo $_SESSION['username']; ?>
    </a>
</li>
<li>
    <a href="api/logout.php"><span class="glyphicon glyphicon-log-in"></span>
        &nbsp; Log Out
    </a>
</li>