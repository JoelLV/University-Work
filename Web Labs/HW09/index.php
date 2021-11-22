<html>
    <head>
        <title>HW09 - Joel Lopez Villarreal</title>
    </head>
    <body>
        <h1>COVID-19 Temperature Check Stations (Highlighted Stations are available)</h1>
        <?php
            $connection = mysqli_connect("localhost", "joell", "squi91xel", "joell_covid_stations") or die("Could not connect");
            $sql = "select * from session INNER JOIN location on session.location = location.location";
            $result = mysqli_query($connection, $sql);
            
            $today = intval(date("N")) + 1;
            if ($today == 8){
                $today = 1;
            }
            $time = intval(date("Gi"));
            
            print("<table border=1><tr><th>Location</th><th>Open Time</th><th>Closing Time</th></tr>");
            while($row = mysqli_fetch_assoc($result)){
                if ($today == $row['dayofweek']){
                    $ontime = "";
                    if ($time >= $row['begintime'] and $time < $row['endtime']){
                        $ontime = " style=\"background-color:lightblue;\"";
                    }
                    print("<tr" . $ontime . ">");
                    print("<td>" . $row['l-name'] . "</td><td>" . $row['begintime'] . "</td><td>" . $row['endtime'] . "</td></tr>");
                }
            }
            print("</table>");
            mysqli_free_result($result);
            mysqli_close($connection);
        ?>
    </body>
</html>