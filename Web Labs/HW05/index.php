<html>
    <head>
        <title>HW05 - Joel Lopez Villarreal</title>
    </head>
    <body>
        <h1>HW05 - Text Analysis</h1>
        <p>List of files:</p>
        <table border="1">
            <tr><th>File Name</th><th>Size</th></tr>
            <?php
                $files = array();
                $dir = "paragraphs";

                if(is_dir($dir)){
                    if($dir_obj = opendir($dir)){
                        while(($file = readdir($dir_obj)) !== false){
                            if($file != "." and $file != ".."){
                                array_push($files, $file);
                            }
                        }
                        closedir($dir_obj);
                    }
                }
                sort($files);
                foreach($files as $file){
                    print("<tr>");
                        print("<td>" . $file . "</td>");
                        print("<td>" . filesize($dir . "/" . $file) . "</td>");
                    print("</tr>");
                }
            ?>
        </table>
        <h1>Word list:</h1>
        <table border="1">
            <tr><th>Word</th><th>Number</th></tr>
            <?php
                $word_counter_list = array();
                foreach($files as $file){
                    $file_content = file_get_contents($dir . "/" . $file);
                    $file_content = str_replace("\n", "", $file_content);
                    $file_content = str_replace("\r", "", $file_content);
                    $file_content = str_replace(",", "", $file_content);
                    $file_content = str_replace(".", "", $file_content);
                    $file_content = str_replace("  ", " ", $file_content);
                    $file_content = trim($file_content);
                    $file_content = strtolower($file_content);

                    $words = explode(" ", $file_content);
                    
                    $checked_words_in_file = array();
                    for($i = 0; $i < sizeof($words); $i++){
                        $word_counter = 0;
                        if(!in_array($words[$i], $checked_words_in_file)){
                            array_push($checked_words_in_file, $words[$i]);
                            for($ii = $i; $ii < sizeof($words); $ii++){
                                if($words[$i] == $words[$ii]){
                                    $word_counter += 1;
                                }
                            }
                        }
                        if(isset($word_counter_list[$words[$i]])){
                            $word_counter_list[$words[$i]] += $word_counter;
                        }
                        else{
                            $word_counter_list[$words[$i]] = $word_counter;
                        }
                    }
                }
                arsort($word_counter_list);
                foreach($word_counter_list as $word => $frequency){
                    print("<tr>");
                        print("<td>" . $word . "</td>");
                        print("<td>" . $frequency . "</td>");
                    print("</tr>\n");
                }
            ?>
        </table>
    </body>
</html>