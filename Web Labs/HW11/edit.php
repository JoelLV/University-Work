<html>
    <head>
        <title>Edit Mode</title>
    </head>
    <body>
        <?php
            print("Edit mode: <br />");
            print("<form method=\"post\" action=\"execute.php\">");
            print("Type new begin time <input type=\"text\" name=\"beginTime\"><br />");
            print("Type new end time <input type=\"text\" name=\"endTime\"><br />");
            print("<input type=\"hidden\" name=\"sessionNum\" value=\"" . $_POST['sessionNum'] . "\">");
            print("<input type=\"submit\" name=\"submit\">");
            print("</form>");
        ?>
    </body>
</html>