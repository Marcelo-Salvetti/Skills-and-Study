document.getElementById("registerForm")?.addEventListener("submit", function(event) {
    event.preventDefault(); // Impede o comportamento padrão do formulário

    let formData = new FormData();
    formData.append("username", document.getElementById("newUsername").value); // Corrigido "usename" para "username"
    formData.append("password", document.getElementById("newPassword").value); // Corrigido "newPassord" para "newPassword"

    fetch("backend/register.php", {
        method: "POST",
        body: formData
    })
    .then(response => response.json()) // Corrigido "jason" para "json"
    .then(data => { // Removido ")" extra
        if (data.status === "success") { // Corrigido "sucess" para "success"
            window.location.href = "login.html";
        } else {
            alert("Erro: " + data.message);
        }
    })
    .catch(error => { // Tratamento de erros no caso de problemas com a requisição
        console.error("Erro na requisição:", error);
        alert("Algo deu errado. Por favor, tente novamente.");
    });
});

// pagina login

document.getElementById("loginForm")?.addEventListener("submit", function(event){
    event.preventDefault();
    let formData = new FormData();
    formData.append("username", document.getElementById("username").value);
    formData.append("password", document.getElementById("password").value);
    
    fetch("backend/login.php", {method: "POST", body:formData})
     .then(response => response.json())
     .then(data => {
        if(data.status === "success"){
            window.location.href = "index.php";
        }else {
            alert("Erro: " + data.message);
        }
     })
});
