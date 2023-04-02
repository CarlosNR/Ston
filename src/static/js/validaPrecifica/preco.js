const validarPreco = async () => {

    const formCadastro = document.forms["precifica"]
    const precoFormElement = formCadastro['novoPreco']
    const preco = Number(precoFormElement.value)

    if(preco >= 0){
        precoFormElement.setCustomValidity("")
    }else{
        precoFormElement.setCustomValidity("Valor invalido, inserir um número igual ou maior que 0.")
        precoFormElement.reportValidity()
    }

}