const validarValor = async () => {

    const formCadastro = document.forms["formPrecifica"]
    const precoFormElement = formCadastro['novoPreco']
    const preco = precoFormElement.value

    if(preco >= 0 && preco !== ""){
        precoFormElement.setCustomValidity("")
    }else{
        precoFormElement.setCustomValidity("Valor invalido, inserir um número igual ou maior que 0.")
        precoFormElement.reportValidity()
    }

}