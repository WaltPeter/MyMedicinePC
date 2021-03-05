<?php 
function connect() {
	$conn = mysqli_connect("remotemysql.com", "JcoNLt0I6V", "uY12VfydAr", "JcoNLt0I6V"); 
	if (mysqli_connect_errno()) {
	     die('Cannot connect to database: ' . mysqli_error()); 
	}

	$conn->set_charset("utf8");
	return $conn; 
}