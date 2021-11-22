<html>
    <head>
        <title>HM02 - Joel Lopez Villarreal</title>
        <link rel="stylesheet" href="style.css" type="text/css">
    </head>
    <body>
        <h1>HW02 - Multiplication Table</h1>
        <?php
            print("<table border='1'>");
                print("<tr>"); #Heading section starts
                    print("<th rowspan='2' colspan='2'>Multiply</th>");
                    for($i = 1; $i <= 20; $i++){
                        print("<th>" . $i . "</th>");
                    }
                print("</tr>");
                print("<tr>");
                    for($i = 1; $i <= 20; $i++){
                        print("<th>" . dechex($i) . "</th>");
                    }
                print("</tr>"); #Heading section ends
                    
                for($i = 1; $i <= 20; $i++){ #Main section starts
                    print("<tr>");
                    print("<th>" . $i . "</th>");
                    print("<th>" . dechex($i) . "</th>");
                    for($ii = 1; $ii <= 20; $ii++){
                        print("<td>" . dechex($i * $ii) . "</td>"); #Multiplication
                    }
                    print("</tr>"); #Main section ends
                }
            print("</table>")
        ?>
    </body>
</html>