<html>
    <head>
        <title>HW04 - Joel Lopez Villarreal</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css" type="text/css">
    </head>
    <body>
        <h1 id="headingComputer">HW04 - for Computers - Joel Lopez Villarreal</h1>
        <h1 id="headingMobile">HW04 - for Cell Phones - Joel Lopez Villarreal</h1>
        <div id=pictureBox>
            <?php
                $pictures = array("Camel.JPG", "Cheetah.JPG", "CuteKitty.gif","Meerkat.JPG", "Otter.JPG", "RedPanda.JPG", "Rhino.JPG", "Tiger.gif", "Zebra.JPG");
                $pictures_rendered_per_row = 0;
                for($i = 0; $i < sizeof($pictures); $i++){
                    print("<img src=\"Images/" . $pictures[$i] . "\" />");
                    ++$pictures_rendered_per_row;
                    if ($pictures_rendered_per_row % 4 == 0){
                        print("<br />");
                    }
                }
            ?>
        </div>
    </body>
</html>