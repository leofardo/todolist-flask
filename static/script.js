function editar(e, id, page, status){

    let linha = e.target.parentElement.parentElement
    if(linha.tagName == 'TD'){
        linha = linha.parentElement
    }

    const posicao = linha.querySelector("td[descricao]").cellIndex
    const descricao = linha.querySelector("td[descricao]").innerHTML;

    linha.querySelector("td[descricao]").remove()

    const td = document.createElement("td");
    const form = document.createElement("form")
    const inputEdit = document.createElement("input");
    const inputSubmit = document.createElement("input");

    inputEdit.setAttribute('type', 'text')
    inputEdit.setAttribute('name', 'descricao')
    inputEdit.setAttribute('style', 'margin-right:2px;')
    inputEdit.value = descricao

    inputSubmit.setAttribute('type', 'submit')

    inputSubmit.value = 'Salvar'

    form.appendChild(inputEdit)
    form.appendChild(inputSubmit)

    form.setAttribute('method', 'POST')
    form.setAttribute('action', 'editar/'+ page + '/' + id + '/' + status)

    td.appendChild(form)

    linha.insertBefore(td, linha.children[posicao]);
}


/* AJUSTANDO O SELECTED DOS BOTOES DE FILTRO */

let urlParams = new URLSearchParams(window.location.search);
let status = urlParams.get('status')
if(status == null){
    status = 'todos'
}
status = 'status-' + status.toLowerCase().replace(/\s+/g, '-');
classesFiltro = document.getElementsByClassName('opcoes-links')[0].children

for (let i = 0; i < classesFiltro.length; i++) {
    if (classesFiltro[i].classList.value == status) {
        classesFiltro[i].classList.add('selected');
    }
}
