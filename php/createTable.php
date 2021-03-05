<?php 
require_once 'dbStructure.php'; 
require_once 'connect.php'; 
$conn = connect(); 

$sql = "CREATE TABLE " . $_POST['table_name'] . " (ID INTEGER PRIMARY KEY AUTO_INCREMENT, "
            . EVENT . " TEXT, " . TIME . " TEXT, " . DATE . " TEXT, " . MONTH . " TEXT, "
            . YEAR . " TEXT)";

if ($conn->query($sql) !== TRUE) {
  echo "Error creating table: " . $conn->error . "<br>" . $sql;
}

mysqli_close($conn);