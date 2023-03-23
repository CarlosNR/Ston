const validarCadastroClienteData = async () => {


    const formCadastro = document.forms["formCadastroCliente"]
    const dataFormElement = formCadastro['nascimento']
    const data = dataFormElement.value
    
    if(/^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$/.test(data)){
        dataFormElement.setCustomValidity("")
    }else{
        dataFormElement.setCustomValidity("data invalida")
        dataFormElement.reportValidity()
    }

}