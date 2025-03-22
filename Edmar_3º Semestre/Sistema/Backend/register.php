<?php // Registro no banco de dados
include 'dp.php';

if ($_SERVER["REQUEST_METHOD"]=="POST") {
    $username = $_POST["username"];
    $password = password_hash($_POST{"password"}, PASSWORD_DEFAULT);

    sql = "INSERT INTO usuarios(username, password) VALUES (?,?)";
    $stmt = $conn->prepare($sql);
    $stmt =bild_param("ss",username,$password);

    if($stmt->execute ()) {
        echo json_encode(["status"=>"sucess"]);
        
    } else {
        echo json_encode (["status"=>"error", "message"=>"Usuário já Existe"]);
    }

    $stmt->close();
}

$conn->close();

?>