<html>
    <head>
        <title>HW11 - Joel Lopez Villarreal</title>
    </head>
    <body>
        <h1>COVID-19 Temperature Check Stations (Highlighted Stations are available)</h1>
        <?php
            $connection = mysqli_connect("localhost", "joell", "squi91xel", "joell_covid_stations") or die("Could not connect");
            if($_POST){
                if(isset($_POST['Delete'])){
                    $sql = "DELETE FROM `session` WHERE `session`.`sessnum` = " . $_POST['Delete'];
                    mysqli_query($connection, $sql);
                }
                else if(isset($_POST['Add'])){
                    $last_session_num = 0;
                    $sql = "select * from session INNER JOIN location on session.location = location.location";
                    $result = mysqli_query($connection, $sql);
                    while($row = mysqli_fetch_assoc($result)){
                        $last_session_num = $row['sessnum'];
                    }
                    $new_session_num = $last_session_num + 1;
                    mysqli_free_result($result);
                    $sql = "INSERT INTO `session` (`sessnum`, `location`, `dayofweek`, `begintime`, `endtime`) VALUES (" . $new_session_num . ", " . $_POST['new_loc'] . ", " . $_POST['new_day_of_week'] . ", " . $_POST['new_begin_time'] . ", " . $_POST['new_end_time'] . ")";
                    if($_POST['new_loc'] != "" and $_POST['new_begin_time'] != "" and $_POST['new_end_time'] != ""){
                        mysqli_query($connection, $sql);
                    }
                    else{
                        print("INVALID INPUT");
                    }
                }
                else if(isset($_POST['Edit'])){
                    print("<form method=\"post\" action=\"edit.php\">");
                    print("Click Button for Edit Mode: <input type=\"submit\" name=\"submit\">");
                    print("<input type=\"hidden\" name=\"sessionNum\" value=\"" . $_POST['Edit'] . "\">");
                    print("</form>");
                }
            }
            $sql = "select * from session INNER JOIN location on session.location = location.location";
            $result = mysqli_query($connection, $sql);
            
            $today = intval(date("N")) + 1;
            if ($today == 8){
                $today = 1;
            }
            $time = intval(date("Gi"));
            
            print("<form method=\"post\" action=\"\">");
            print("<table border=1><tr><th>Delete</th><th>Edit</th><th>Location</th><th>Open Time</th><th>Closing Time</th></tr>");
            while($row = mysqli_fetch_assoc($result)){
                if ($today == $row['dayofweek']){
                    $ontime = "";
                    if ($time >= $row['begintime'] and $time < $row['endtime']){
                        $ontime = " style=\"background-color:lightblue;\"";
                    }
                    print("<tr" . $ontime . ">");
                    print("<td><button type=\"submit\" name=\"Delete\" value=\"" . $row['sessnum'] . "\">Delete</button></td>
                        <td><button type=\"submit\" name=\"Edit\" value=\"" . $row['sessnum'] . "\">Edit</button></td>
                        <td>" . $row['l-name'] . "</td><td>" . $row['begintime'] . "</td><td>" . $row['endtime'] . "</td></tr>");
                }
            }
            print("</table>");
            mysqli_free_result($result);

            $sql = "SELECT * FROM `location`";
            $result = mysqli_query($connection, $sql);

            print("Enter New Location:<br />");
            print("<select name=\"new_loc\">");
            while($row = mysqli_fetch_assoc($result)){
                print("<option value=\"" . $row['location'] . "\">" . $row['l-name'] . "</option>");
            }
            print("</select><br />");
            mysqli_free_result($result);
            
            print("Enter Day for New Session:<br />");
            print("<select name=\"new_day_of_week\">");
                print("<option value=\"1\" selected>Sunday</option>");
                print("<option value=\"2\">Monday</option>");
                print("<option value=\"3\">Tuesday</option>");
                print("<option value=\"4\">Wednesday</option>");
                print("<option value=\"5\">Thursday</option>");
                print("<option value=\"6\">Friday</option>");
                print("<option value=\"7\">Sabbath</option>");
            print("</select><br />");
            print("Enter Begin Time and End Time of New Session:<br /><input type=\"text\" name=\"new_begin_time\"> to <input type=\"text\" name=\"new_end_time\"><br />");
            print("<input type=\"submit\" name=\"Add\" value=\"Add new session\">");
            print("</form>");

            mysqli_close($connection);
        ?>
    </body>
</html>