const validarCadastroJogoGenero = async () => {

    const formCadastro = document.forms["formCadastraJogo"]
    const generoFormElement = formCadastro['genero']
    const genero = generoFormElement.value

    if(/^[A-z ]+$/.test(genero)){
        generoFormElement.setCustomValidity("")
    }else{
        generoFormElement.setCustomValidity("Genero invalido.")
        generoFormElement.reportValidity()
    }

}