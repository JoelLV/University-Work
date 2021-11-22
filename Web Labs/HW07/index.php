<html>
    <head>
        <title>HW07 - Joel Lopez Villarreal</title>
    </head>
    <body>
        <h1>HW07 - Uploading - Joel Lopez Villarreal</h1>
        <form action="" name="upload" method="POST" enctype="multipart/form-data">
        Select file to upload: <input type="file" name="fileToUpload">
        <input type="submit" name="submit" value="Upload File"><br />
        <?php
            $files_uploaded = array();
            $files_published = array();
            $target_dir = "uploads";
            $target_dir_publ = "publish";
            if($_POST){
                $file_type = "image";
                $target_file = $target_dir . "/" . $_FILES['fileToUpload']['name'];
                $ready_to_upload = true;
                
                if(substr($_FILES['fileToUpload']['type'], 0, 5) !== $file_type){
                    #print("Error: File is not an image <br />");
                    $ready_to_upload = false;
                }
                if(sizeof($files_uploaded) > 0){
                    if(file_exists($target_file)){
                        #print("Error: File has already been uploaded <br />");
                        $ready_to_upload = false;
                    }
                }

                if($ready_to_upload){
                    if(move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)){
                        #print("File successfully uploaded <br />");
                    }
                    else{
                        print("Error: File could not be uploaded <br />");
                    }
                }
            }

            if(is_dir($target_dir)){
                if($dir = opendir($target_dir)){
                    while($file = readdir($dir)){
                        if($file != "." and $file != ".."){
                            array_push($files_uploaded, $file);
                        }
                    }
                    closedir($dir);
                }
            }
            if(is_dir($target_dir_publ)){
                if($dir = opendir($target_dir_publ)){
                    while($file = readdir($dir)){
                        if($file != "." and $file != ".."){
                            array_push($files_published, $file);
                        }
                    }
                    closedir($dir);
                }
            }

            $index = 0;
            foreach($files_uploaded as $file){
                $file_name_in_post = str_replace(" ", "_", $file);
                $file_name_in_post = str_replace(".", "_", $file_name_in_post);
                if(isset($_POST[$file_name_in_post])){
                    if($_POST[$file_name_in_post] == 'Delete'){
                        unlink("uploads/" . $file);
                        unset($files_uploaded[$index]);
                    }
                    if($_POST[$file_name_in_post] == 'Publish'){
                        rename("uploads/" . $file, "publish/" . $file);
                        array_push($files_published, $file);
                        unset($files_uploaded[$index]);
                    }
                    break;
                }
                $index += 1;
            }
            $index = 0;
            foreach($files_published as $file){
                $file_name_in_post = str_replace(" ", "_", $file);
                $file_name_in_post = str_replace(".", "_", $file_name_in_post);
                if(isset($_POST[$file_name_in_post])){
                    if($_POST[$file_name_in_post] == 'Delete'){
                        unlink("publish/" . $file);
                        unset($files_published[$index]);
                    }
                    break;
                }
                $index += 1;
            }
            if(sizeof($files_uploaded) > 0){
                print("<b>Current uploads</b><br />");
                print("<table border=1>");
                    print("<tr><th></th><th>File name</th><th>Size</th><th></th></tr>\n");
                        foreach($files_uploaded as $file){
                            print("<tr><td><input type=\"submit\" name=\"" . $file . "\" value=\"Delete\"><br /><input type=\"submit\" name=\"" . $file . "\" value=\"Publish\"></td>\n");
                            print("<td><a href=\"uploads/" . $file . "\" target=\"_blank\">" . $file ."</td>\n");
                            print("<td>" . filesize("uploads/" . $file) . "</td>\n");
                            print("<td><a href=\"uploads/" . $file . "\" target=\"_blank\"><img src=\"uploads/" . $file . "\"height=\"auto\" width=\"200\" /></a></td></tr>\n");
                        }
                print("</table>");
            }
            if(sizeof($files_published) > 0){
                print("<b>Current published</b>");
                print("<table border=1");
                    print("<tr><th></th><th>File name</th><th>Size</th><th></th></tr>\n");
                        foreach($files_published as $file){
                            print("<tr><td><input type=\"submit\" name=\"" . $file . "\" value=\"Delete\"></td>\n");
                            print("<td><a href=\"publish/" . $file . "\" target=\"_blank\">" . $file ."</td>\n");
                            print("<td>" . filesize("publish/" . $file) . "</td>\n");
                            print("<td><a href=\"publish/" . $file . "\" target=\"_blank\"><img src=\"publish/" . $file . "\"height=\"auto\" width=\"200\" /></a></td></tr>\n");
                        }
                print("</table>");
            }
        ?>
        </form>
    </body>
</html>
