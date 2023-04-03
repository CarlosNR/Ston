const validarCadastroJogoNome = async () => {


    const formCadastro = document.forms["formCadastraJogo"]
    const nomeFormElement = formCadastro['nome']
    const nome = nomeFormElement.value

    if(/^[A-z ]+$/.test(nome)){
        nomeFormElement.setCustomValidity("")
    }else{
        nomeFormElement.setCustomValidity("Nome invalido.")
        nomeFormElement.reportValidity()
    }

}