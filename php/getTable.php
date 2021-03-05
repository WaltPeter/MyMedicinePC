<?php
require_once 'connect.php'; 

$conn = connect(); 

$sql = "SELECT patient_id, name FROM patient_info";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<br> id: ". $row["patient_id"]. " - Name: ". $row["name"] . "<br>";
    }
} else {
    echo "0 results";
}

mysqli_close($conn);
?>