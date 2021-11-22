<html><head><title>Database Demo #1</title></head>
<body>
<?php
$conn=mysqli_connect("localhost","joell","squi91xel","joell_T2") or die("Could not open database");
if ($_POST) {
  print "<pre>POST:"; print_r($_POST); print "</pre>";
  if (isset($_POST['Add'])) {
    print "We will add something<br />";
    // INSERT INTO `StateList` (`StateCode`, `StateName`) VALUES ('BC', 'British Columbia');
    // INSERT INTO `StateList` (`StateCode`, `StateName`, `regioncode`) 
    //      VALUES ('ON', 'Ontario', 'C'); 
    $sql="INSERT INTO `StateList` (`StateCode`, `StateName`, `regioncode`, `langcode`) " . 
          "VALUES ('" . $_POST['statecode'] . "', '" . $_POST['statename'] . "', '" . $_POST['Region'] . "', '" . $_POST['language'] . "');";
    print "Add sql: " . $sql . "<br />";
    if (mysqli_query($conn, $sql)) {
      echo "New record created successfully";
    } else {
       echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }
  } else {
    $sql = "SELECT * from StateList WHERE StateCode = \"" . $_POST['DELETE'] . "\";";
    $result = mysqli_query($conn,$sql);
    $row = mysqli_fetch_assoc($result);
    print "We are deleting " . $_POST['DELETE'] . ":" . $row['StateName'] . "<br />";
    $sql = "DELETE FROM `StateList` WHERE `StateList`.`StateCode` = '" . $_POST['DELETE'] . "';";
    //  print "SQL:" . $sql . "<br />";
    $result=mysqli_query($conn,$sql);
  } // end of delete section
}
print "<form method=\"POST\">";
$sql = "select * from StateList ORDER BY StateName;";
//print "SQL:" . $sql . "<br />";
$result = mysqli_query($conn,$sql);
// $row = mysqli_fetch_assoc($result);
print "<table border=1><tr><th></td><th>Code</th><th>Name</th><th>Language</th></tr>";
while ($row = mysqli_fetch_assoc($result)) {
// <button name="DELETE" type="submit" value="72">Delete</button>
  $delstate = $row['StateCode'];
  print "<tr><td><button name=\"DELETE\" type=\"submit\" value=\"" . $delstate . "\">Delete</button>" . "</td><td>" . $row['StateCode'] . "</td><td>" . $row['StateName'] . 
        "</td><td>" . $row['langcode'] . "</td></tr>\n";   #CHANGE
}
//mysqli_close($conn);
?>
</form>
</table>
<form method="POST">
State code:<input type="text" name="statecode"><br />
State name:<input type="text" name="statename"><br />
<?php
//<select name="cars" id="cars">
//  <option value="volvo">Volvo</option>
//  <option value="saab">Saab</option>
//  <option value="mercedes">Mercedes</option>
//  <option value="audi">Audi</option>
//</select> 
print "<select name=\"Region\">\n";
$sql = "SELECT * FROM `regions` ";
$result=mysqli_query($conn,$sql);
while ($row=mysqli_fetch_assoc($result)) {
  print "<option value=\"" . $row['regioncode'] . "\">" . $row['regionname'] . "</option>\n";
}
print "</select>\n";

$sql = "SELECT * FROM `language`";
$result = mysqli_query($conn,$sql);
print("Language:");
print("<select name=\"language\">");
    while($row = mysqli_fetch_assoc($result)){
        print("<option value=\"" . $row['langcode'] . "\">" . $row['language'] . "</option>");
    }
print("</select><br />");
mysqli_close($conn);
?>
<input type="submit" name="Add">
</form>
</body></html>