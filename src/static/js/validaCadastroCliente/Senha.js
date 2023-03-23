const validarCadastroClienteSenha = async () => {

    const formCadastro = document.forms["formCadastroCliente"]
    const senhaFormElement = formCadastro['senha']
    const senha = senhaFormElement.value

    if(senha.length < 6){
        senhaFormElement.setCustomValidity("senha invalida, inserir pelo menos 6 digitos.")
        senhaFormElement.reportValidity()
    }else{
        senhaFormElement.setCustomValidity("")
    }

}
