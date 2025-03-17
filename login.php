<?php
// Establecer la conexión a la base de datos
$servername = "localhost";
$username = "tu_usuario";
$password = "tu_contraseña";
$dbname = "directorio_comercios";

$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar la conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Consulta SQL para obtener los comercios
$sql = "SELECT id, nombre, descripcion, imagen_url FROM comercios";
$result = $conn->query($sql);

?>
