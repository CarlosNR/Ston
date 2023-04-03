const validarCadastroJogoPreco = async () => {

    const formCadastro = document.forms["formCadastraJogo"]
    const precoFormElement = formCadastro['preco']
    const preco = precoFormElement.value

    if(preco > 0){
        precoFormElement.setCustomValidity("")
    }else{
        precoFormElement.setCustomValidity("Valor invalido, inserir um número igual ou maior que 0.")
        precoFormElement.reportValidity()
    }

}