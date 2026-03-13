function verificar() {
    // Na linha 16 do modelo.html, estva faltando o id="txtano" em <input type="number" name="txtano" BEM AQUI min="0"> 
    // Era por isso que eu clicava no botão e não acontecia nada!!! Obrigado Geminiiiiii 
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano') // Como esqueci do id="txtano", podia ter colocado document.getElementByName, que 
    var res = document.querySelector('div#res') // funcionaria!! Mas enfim...
    console.log(res) // Isso é para exibir na tela ??
    if (fano.value.length == 0 || Number(fano.value) > ano) {
        window.alert('[ERRO] Verifique os dados e tente novamente!')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value) /* isso é o valor digitado em fano */
        var gênero = ''
        var img = document.createElement('img') // Isso é para colocar a imagem dinamicamente (por JS!)
        img.setAttribute('id', 'foto')
        if (fsex[0].checked) { // Ou seja, se o que estiver marcado (checkado) for o fsex[0], será um homem!
            gênero = 'Homem'
            if (idade >= 0 && idade < 10) { 
                // é uma criança
                img.setAttribute('src', 'foto-bebe-m.png') // 'src' pq é o source da imagem!!
            } else if (/*Poderia colocar idade >= 10 && */idade < 21 ) { 
                // é um jovem
                img.setAttribute('src', 'foto-jovem-m.png')
            } else if (idade < 50) { 
                // é um adulto
                img.setAttribute('src', 'foto-adulto-m.png')
            } else { 
                // é um idoso
                img.setAttribute('src', 'foto-idoso-m.png')
            }
        } else if (fsex[1].checked) { // Caso contrário, será mulher!
            gênero = 'Mulher'
            if (idade >= 0 && idade < 10) { 
                // é uma criança
                img.setAttribute('src', 'foto-bebe-f.png')
            } else if (idade < 21 ) { 
                // é uma jovem
                img.setAttribute('src', 'foto-jovem-f.png')
            } else if (idade < 50) { 
                // é uma adulta
                img.setAttribute('src', 'foto-adulto-f.png')
            } else { 
                // é uma idosa
                img.setAttribute('src', 'foto-idoso-f.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${gênero} com ${idade} anos.`
        res.appendChild(img) // Isso é para adicionar um elemento, que é o (img).
    } 

}
