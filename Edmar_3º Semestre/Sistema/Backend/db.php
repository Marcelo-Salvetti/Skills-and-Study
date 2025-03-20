<?php
$servername = "root";
$username = "root";
$password = "Root";
$database = "sistem";

$conn = new mysqli($servername,$username, $password, $database);

if($conn -> connect_erro){
    die("Falha na Conexão: ".$conn -> connect_error);
}

?>