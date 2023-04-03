const validarCadastroJogoPublicadora = async () => {

    const formCadastro = document.forms["formCadastraJogo"]
    const publicadoraFormElement = formCadastro['publicadora']
    const publicadora = publicadoraFormElement.value

    if(/^[A-z ]+$/.test(publicadora)){
        publicadoraFormElement.setCustomValidity("")
    }else{
        publicadoraFormElement.setCustomValidity("Publicadora invalida.")
        publicadoraFormElement.reportValidity()
    }

}