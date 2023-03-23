const validarCadastroClienteNome = async () => {


    const formCadastro = document.forms["formCadastroCliente"]
    const nomeFormElement = formCadastro['nome']
    const nome = nomeFormElement.value

    if(/^[A-z ]+$/.test(nome)){
        nomeFormElement.setCustomValidity("")
    }else{
        nomeFormElement.setCustomValidity("nome invalido")
        nomeFormElement.reportValidity()
    }

}