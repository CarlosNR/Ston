function validarEmail(email, emailFormElement){
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)){
        return true
    }
    else{
        emailFormElement.setCustomValidity("email invalido")
        emailFormElement.reportValidity()
        return false
    }      
}

const validarCadastroClienteEmail = async () => {

    const formCadastro = document.forms["formCadastroCliente"]
    const emailFormElement = formCadastro['email']
    const email = emailFormElement.value
    
    respJs = validarEmail(email, emailFormElement)
    if(respJs){
        axios.post('/insert/cliente/valida/email', {
            email: email
        })
        .then((response) => {
            // console.log("")
            // console.log(response.data.emailNaoRepetido)
            if(response.data.emailRepetido == "true"){
                emailFormElement.setCustomValidity("email já cadastrado")
                emailFormElement.reportValidity()
            }else{
                emailFormElement.setCustomValidity("")
            }
        }, (error) => {
            console.log(error)
        })
    
    }

}