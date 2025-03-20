document.getElementById("registerForm")?.addEventListener("submit", function(event){

    event.preventDefault();

    let formData = new FormData();
    formData.append("usename", document. getElementById("newUsername").value);
    formData.append("password", document. getElementById("newPassord").value);

    fetch("backend/register.php",{method: "POST", body:formData})
    .then(response=>response.jason())
    .then(data =>) {
        if(data.status === "sucess"){window.location.href = "login.html";}
        else {
            alert("Erro: " + data.message);
        }
          
    }]);

});