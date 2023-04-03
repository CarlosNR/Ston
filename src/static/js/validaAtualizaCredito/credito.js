const validarCredito = async () => {
    const formCadastro = document.forms["formCredita"]
    const precoFormElement = formCadastro['creditoAdicional']
    const preco = precoFormElement.value

    if(preco >= 0 && preco !== ""){
        precoFormElement.setCustomValidity("")
    }else{
        precoFormElement.setCustomValidity("Valor invalido, inserir um número igual ou maior que 0.")
        precoFormElement.reportValidity()
    }

}