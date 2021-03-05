<?php
require_once 'connect.php'; 
$conn = connect(); 

$sql = "SELECT * FROM `patient_info` WHERE `ID`=" . $_POST['patient_id'];
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo json_encode($row); 
    }
} else {
    echo "No result.";
}

mysqli_close($conn);
?>