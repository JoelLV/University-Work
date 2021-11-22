<html>
    <head>
        <title>HW08 - Joel Lopez Villarreal</title>
    </head>
    <body>
        <h1>Bible Text Lookup</h1>
        <form action="" method="POST">
        <?php
            #print_r($_POST);
            $connection = new mysqli("localhost", "joell", "squi91xel", "joell_bible") or die("Cannot connect to db");
            $sql_bible_versions = "SELECT * FROM `bible_version_key`";

            $result_bible_versions = mysqli_query($connection, $sql_bible_versions);

            print("<select name=\"Bible_ver\">\n");
            while($row = mysqli_fetch_assoc($result_bible_versions)){
                $selected = "";
                if(isset($_POST['Bible_ver'])){
                    if($_POST['Bible_ver'] == $row['abbreviation']){
                        $selected = " selected";
                    }
                }
                if(!$_POST and $row['abbreviation'] == 'KJV'){
                    print("<option value=\"" . $row['abbreviation'] . "\" selected>". $row['abbreviation'] . "</option>\n");
                }
                else{
                    print("<option value=\"" . $row['abbreviation'] . "\"" . $selected . ">" . $row['abbreviation'] . "</option>\n");
                }
            }
            print("</select>\n");
            
            print(" Citation: ");
            $selected = "";
            if(isset($_POST['bible_citation'])){
                $selected = $_POST['bible_citation'];
            }
            print("<input type=\"text\" name=\"bible_citation\" value=\"" . $selected . "\">\n");
            print("<input type=\"submit\" name=\"submit\"><br />\n");

            print("</form>");

            if($_POST){
                $name_of_version = "";
                $version_in_db = "";
                $book_found = false;
                $citation_found = false;
                $result_bible_versions = mysqli_query($connection, $sql_bible_versions);

                while($row = mysqli_fetch_assoc($result_bible_versions)){
                    if($row['abbreviation'] == $_POST['Bible_ver']){
                        $name_of_version = $row['version'];
                        $version_in_db = $row['table'];
                        break;
                    }
                }
                print("<b>" . $name_of_version . "</b><br />");
                
                $sql_bible_texts = "SELECT * FROM `" . $version_in_db . "`";
                $sql_bible_book_name = "SELECT * FROM `key_english`";
                $sql_bible_book_abb = "SELECT * FROM `key_abbreviations_english`";
                $result_bible_text = mysqli_query($connection, $sql_bible_texts);
                $result_bible_book_name = mysqli_query($connection, $sql_bible_book_name);
                $result_bible_book_abb = mysqli_query($connection, $sql_bible_book_abb);
                
                $user_bible_citation = strrev($_POST['bible_citation']);
                $user_bible_citation = explode(" ", $user_bible_citation, 2);
                $user_bible_book = strrev($user_bible_citation[1]);
                $user_bible_nums = strrev($user_bible_citation[0]);
                
                $bible_chapter = "";
                $bible_verse = "";
                if(strpos($user_bible_nums, ":")){
                    $user_bible_nums = explode(":", $user_bible_nums);
                    $bible_chapter = $user_bible_nums[0];
                    $bible_verse = $user_bible_nums[1];
                }
                else{
                    $bible_chapter = "1";
                    $bible_verse = $user_bible_nums;
                }
                
                $book_key = "";
                while($row = mysqli_fetch_assoc($result_bible_book_name)){
                    if($user_bible_book == $row['n']){
                        $book_key = $row['b'];
                        $book_found = true;
                        break;
                    }
                }
                if(!$book_found){
                    while($row = mysqli_fetch_assoc($result_bible_book_abb)){
                        if($user_bible_book == $row['a']){
                            $book_key = $row['b'];
                            $book_found = true;
                            break;
                        }
                    }
                }

                if($book_found){
                    while($row = mysqli_fetch_assoc($result_bible_text)){
                        if(($row['b'] == $book_key) and ($row['c'] == $bible_chapter) and ($row['v'] == $bible_verse)){
                            $citation_found = true;
                            print($row['t']);
                            break;
                        }
                    }
                }
                if(!$citation_found){
                    print("Citation not found");
                }
                mysqli_free_result($result_bible_text);
                mysqli_free_result($result_bible_book_name);
                mysqli_free_result($result_bible_book_abb);
            }
            mysqli_free_result($result_bible_versions);
            mysqli_close($connection);
        ?>
    </body>
</html>