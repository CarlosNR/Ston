const validarCadastroClienteCredito = async () => {

    const formCadastro = document.forms["formCadastroCliente"]
    const creditoFormElement = formCadastro['credito']
    const credito = creditoFormElement.value

    if(credito > 0){
        creditoFormElement.setCustomValidity("")
    }else{
        creditoFormElement.setCustomValidity("credito invalido, inserir um número.")
        creditoFormElement.reportValidity()
    }

}