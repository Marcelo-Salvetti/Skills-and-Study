const form= document.getElementById ("formTarefa");
const input= document.getElementById("inputTarefa");
const lista= document.getElementById("listaTarefa");
const botoesFiltro= document.querySelectorAll(".filtros button");
const toggleTema= document.getElementById("toggleTema");

let tarefas = JSON.parse(localStorage.getItem("tarefas"))|| [];
let filtroAtual = "todas";

function salvarTarefas(){
    localStorage.setItem ("tarefas", JSON.stringify(tarefas));
}

function renderizarTarefas(){
    lista.innerHTML= "";
    let tarefasFiltradas= tarefas.filter(t => {
        if (filtroAtual === "todas") return true;
        if (filtroAtual === "concluidas") return t.concluida;
        if (filtroAtual === "pendentes") return !t.concluida;
    });
    tarefasFiltradas.forEach((tarefa, i ) => {
        const li = document.createElement("li");
        li.className= tarefa.concluida ? "concluida" : "";
        li.innerHTML= `
        <span>${tarefa.texto}</span>
        <div>
        <button onclick="toggleConclusao(${i})">v</button>
        <button onclick="deletarTarefa(${i})">x</button>
        </div>
        `;
        lista.appendChild(li);

});
}

function adicionarTarefa(texto){
    tarefas.push({ texto, concluida: false });
    salvarTarefas();
    renderizarTarefas();
}
form.addEventListener("submit", e => {
    e.preventDefault();
    if (input.value.trim() === "") return;{
        adicionarTarefa(input.value.trim());
        input.value= "";
    }

});