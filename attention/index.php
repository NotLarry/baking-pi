 <?php
    if (isset($_POST['page']))
    {
         system("gpio -g mode 17 out");
        system("gpio -g write 17 0");
    	sleep (10);
	system("gpio -g write 17 1");
	}
    else if (isset($_POST['lights']))
    {
system("gpio -g mode 25 out");
        system("gpio -g write 25 0");
        sleep (10);
        system("gpio -g write 25 1");    
}
?>
<html>
<body>
    <form method="post">
    <p>
        <button name="page">Trigger Warren's latent epilepsy</button>
        <button name="lights">Turn Warren's Glowstone On</button>
    </p>
    
</form>
</body>
</html>
