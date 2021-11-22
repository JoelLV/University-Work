<html>
    <head>
        <title>HW06 - Joel Lopez Villarreal</title>
    </head>
    <body>
        <h1>HW06 - Telephone Exchanges</h1>
        <form action="" method="POST">
        <?php
            $city_chosen = "";
            $state_chosen = "";
            if($_POST){
                //print_r($_POST);
                if(isset($_POST['city'])){
                    $city_chosen = $_POST['city'];
                }
                if(isset($_POST['state'])){
                    $state_chosen = $_POST['state'];
                }
            }
            print("City: ");
            print("<input type=\"text\" name=\"city\" value=\"" . $city_chosen . "\">");
            
            print("State: ");
            print("<input type=\"text\" name=\"state\" value=\"" . $state_chosen . "\"");
            print("<br />");

            print("<input type=\"submit\">");
        ?>
        </form>
        <?php
            if($_POST){
                $data_file = "allutlzd.txt";
                $results_file = "results.txt";
                $data = fopen($data_file, "r") or die("File not found");
                $result = fopen($results_file, "w") or die("File could not be created");
                fgets($data);
                while(! feof($data)){
                    $line = fgets($data);
                    $line = explode("\t", $line);
                    for($i = 0; $i < sizeof($line); $i++){
                        $line[$i] = trim($line[$i]);
                    }
                    if(($state_chosen == $line[0]) and ($city_chosen == $line[4])){
                        $phone_numbers = explode("-", $line[1]);
                        print($phone_numbers[0] . ":" . $phone_numbers[1] . ":" . $line[0] . ":" . $line[4] . "<br />");
                        $line_to_write_in_file = $phone_numbers[0] . ":" . $phone_numbers[1] . ":" . $line[0] . ":" . $line[4] . "\n";
                        fwrite($result, $line_to_write_in_file);
                    }
                }
                fclose($result);
                fclose($data);
                print("<a href=\"results.txt\" download><button>Download</button></a>");
            }
        ?>
    </body>
</html>