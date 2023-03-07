function validarEmail(email, emailFormElement){
    return true
    // // deu certo
    // emailFormElement.setCustomValidity("formato de email invalido")
    // return emailFormElement.reportValidity()
    // // deu ruim
    // return emailFormElement.setCustomValidity("")
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
            console.log("")
            console.log(response.data.emailNaoRepetido)
            if(response.data.emailRepetido == "true"){
                console.log("entrou no if")
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