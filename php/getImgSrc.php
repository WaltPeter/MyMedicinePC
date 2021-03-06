<?php
require_once 'connect.php'; 
$conn = connect(); 

$sql = 'SELECT `img_src` FROM `medicine_info` WHERE `ID`="' . $_POST['ID'] . '"';
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo $row["img_src"]; 
    }
} else {
    echo "No result.";
}

mysqli_close($conn);
?>