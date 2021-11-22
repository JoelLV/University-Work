<html>
    <head>
        <title>HM03 - Joel Lopez Villarreal</title>
    </head>
    <body>
        <h1>HW03 - Multiplication Table</h1>
        <form method='POST' action=''>
        <?php
            $colors = array("white" => "background-color: white;", "lightblue" => "background-color: lightblue", "yellow" => "background-color: yellow;", "coral" => "background-color: coral;", "lightgreen" => "background-color: lightgreen;");
            $previous_color_selection = array("white" => "", "lightblue" => "", "yellow" => "", "coral" => "", "lightgreen" => "");

            if ($_POST and isset($_POST['color'])){
                foreach($previous_color_selection as $color => $selection){
                    if($color == $_POST['color']){
                        $background = $color;
                        $previous_color_selection[$color] = "selected";
                        break;
                    }
                }
            }
            
            print("Select your background: Background:");
            print("<select name=\"color\">");
            foreach($colors as $color => $color_value){
                print("<option " . $previous_color_selection[$color] . " value=\"". $color ."\">" . $color . "</option>");
            }
            print("</select>");

            print("<br />Select the number base: ");
            for($i = 2; $i <= 16; $i++){
                print("<input type=\"submit\" name=\"base\" value=\"" . $i . "\">");
            }
        ?>
        </form>
        <?php
            if($_POST){
                print("<table border='1' style=\"" . $colors[$background] ."\">");
                    print("<tr>"); #Heading section starts
                        print("<th rowspan='2' colspan='2'>Multiply</th>");
                        for($i = 1; $i <= 20; $i++){
                            print("<th>" . $i . "</th>");
                        }
                    print("</tr>");
                    print("<tr>");
                        for($i = 1; $i <= 20; $i++){
                            print("<th>" . base_convert($i, 10, $_POST['base']) . "</th>");
                        }
                    print("</tr>"); #Heading section ends
                        
                    for($i = 1; $i <= 20; $i++){ #Main section starts
                        print("<tr>");
                        print("<th>" . $i . "</th>");
                        print("<th>" . base_convert($i, 10, $_POST['base']) . "</th>");
                        for($ii = 1; $ii <= 20; $ii++){
                            print("<td>" . base_convert(($i * $ii), 10, $_POST['base']) . "</td>"); #Multiplication
                        }
                        print("</tr>"); #Main section ends
                    }
                print("</table>");
            }
        ?>
    </body>
</html>