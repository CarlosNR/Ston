const validarId = async () => {

    const formCadastro = document.forms["formBuscaIdCliente"]
    const idFormElement = formCadastro['id']
    const id = Number(idFormElement.value)
    console.log(id)
    if(id > 0){
        idFormElement.setCustomValidity("")
    }else{
        idFormElement.setCustomValidity("id invalido, inserir um número maior que 0.")
        idFormElement.reportValidity()
    }

}