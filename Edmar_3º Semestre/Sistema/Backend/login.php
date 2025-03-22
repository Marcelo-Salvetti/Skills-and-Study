<?php // Codificando o Login
include 'db.php';

if ($_SERVER['REQUEST_METHOD'] =="POST"){
    $username = $_POST['username'];
    $password = $_POST['password'];

    $sql = "SELECT * FROM usuarios WHERE username = ?";
    $stmt = $conn -> prepare($sql);
    $stmt -> bind_param('s', $username);
    $stmt -> execute();

    $result = $stmt -> get_result();
    if ($result -> num_rows > 0 ) {
        $user = $result -> fetch_assoc();
        
        if (password_verify($password, $user["password"])){
            session_start();
            $_SESSION["username"] = $user
            echo json_encode(["status"=>"sucess"]);
        } else {
            echo json_encode(["status"=>"error", "message"=>"Senha Incorreta"]);
        }
    }
}

$conn -> close();

?>