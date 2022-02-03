var link = "https://rsa-cryptographer.herokuapp.com/" 

function encriptar() {
    const msg = document.getElementById("texto-encriptar").value
    const N = document.getElementById("N").value
    const E = document.getElementById("encE").value
    const url=`${link}/encriptar`
    const data = {
        "msg": msg,
        "N": N,
        "E": E
    }

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body:JSON.stringify(data)
    })
    .then(response => response.json())
    .then(mensagemEncriptada => {
        console.log("Mensagem encriptada:")
        console.log(mensagemEncriptada)
        mensagemErro = document.getElementById("msg-erro-enc")
        mensagemErro.style.color = "green"
        mensagemErro.innerText = "Done!"
        document.getElementById("texto-encriptado").value = mensagemEncriptada["msg"]
    })
}
    
function decriptar() {
    const msg = document.getElementById("texto-decriptar").value
    const P = document.getElementById("P").value
    const Q = document.getElementById("Q").value
    const E = document.getElementById("E").value
    const url=`${link}/desencriptar`
    const data = {
        "msg": msg,
        "P": P,
        "Q": Q,
        "E": E
    }

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body:JSON.stringify(data)
    })
    .then(response => response.json())
    .then(mensagemDesencriptada => {
        mensagemErro = document.getElementById("msg-erro-dec")
        mensagemErro.style.color = "green"
        mensagemErro.innerText = "Done!"
        console.log("Mesagem desencriptada:")
        console.log(mensagemDesencriptada)
        document.getElementById("texto-decriptado").value = mensagemDesencriptada["msg"]
    })

}

function gerarPublica() {
    document.getElementById("msg-erro").innerText = ""
    const P = document.getElementById("pubP").value
    const Q = document.getElementById("pubQ").value
    const E = document.getElementById("pubE").value
    const url=`${link}/gerar`

    const data = {
        "P": P,
        "Q": Q,
        "E": E
    }

    fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(resposta => {
        console.log("Chave gerada:")
        console.log(resposta)
        erro = resposta["erro"]
        mensagemErro = document.getElementById("msg-erro")
        if(erro) {
            mensagemErro.style.color = "red"
            mensagemErro.innerText = resposta["msg"]
            return
        }
        mensagemErro.style.color = "green"
        mensagemErro.innerText = "Done!"
        document.getElementById("showN").value = resposta["N"]
        document.getElementById("showE").value = resposta["E"]
    })
}