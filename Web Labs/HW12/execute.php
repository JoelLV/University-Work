<html>
    <head>
        <title>Execution Window</title>
    </head>
    <body>
        <?php
            $connection = mysqli_connect("localhost", "joell", "squi91xel", "joell_covid_stations") or die("Could not connect");
            $sql = "UPDATE `session` SET `begintime` = '" . $_POST['beginTime'] . "', `endtime` = '" . $_POST['endTime'] . "' WHERE `session`.`sessnum` = " . $_POST['sessionNum'];
            mysqli_query($connection, $sql);
            print("Database was updated<br />");
            print("<a href=\"index.php\">Click here to go back to home page</a>");
        ?>
    </body>
</html>
