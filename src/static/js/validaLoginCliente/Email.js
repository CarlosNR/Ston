const validarLoginClienteEmail = async () => {

    const formLogin = document.forms["formLoginCliente"]
    const emailFormElement = formLogin['email']
    const email = emailFormElement.value
    
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)){
        emailFormElement.setCustomValidity("")
    }
    else{
        emailFormElement.setCustomValidity("email invalido")
        emailFormElement.reportValidity()
    }   

}