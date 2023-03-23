const validarLoginClienteSenha = async () => {

    const formLogin = document.forms["formLoginCliente"]
    const senhaFormElement = formLogin['senha']
    const senha = senhaFormElement.value

    if(senha.length < 6){
        senhaFormElement.setCustomValidity("senha invalida, inserir pelo menos 6 digitos.")
        senhaFormElement.reportValidity()
    }else{
        senhaFormElement.setCustomValidity("")
    }

}
