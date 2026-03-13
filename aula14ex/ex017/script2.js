function contar() {
    // Lembre-se: para facilitar para o back-end, use names tipo assim: name="txtano". 
    // LVR: Isso porque linguagens como PHP aproveitam melhor o name.
    // LVR: estrutura: é txt + as primeiras letras abreviadas do campo que você está trabalhando ou 
    // pegando a informação (getElementBy...), nesse caso é do campo "ano". Mas pode ser a primeiral letra tbm!
    // ex: var inicio = document.getElementById('txti')
    var inicio = document.getElementById('nbrini')
    var fim = document.getElementById('nbrfim') // LVR: para o if funcionar, esses 3 comandos não podem ter o .value
    var passo = document.getElementById('nbrpas') // (porque já tem o .value.length no if!!).
    var res = document.getElementById('res') // 2. Esse aqui não precisa de .value
    // 1. Não estava acontecendo nada quando eu apertava o botão "Contar" porque faltava o .value nas variáveis acima!!!
    // o .value!!!!!!!!!!!!!!!!
    // 2. Percebi que o var res = document.... não precisa do .value!! Acho que é porque é texto, o conteúdo!!
    // console.log(res) - LVR: esse carinha é inútil nesse código!
    // if (inicio == '' || fim == '') { // isso valida os dados! Testa se o usuário colocou algo nesse campo!
        // res.innerHTML = `Impossível contar!` // para isso funcionar, não pode ter .value no var res = document.....
    // LVR: esse meu validador de dados não estava funcionando porque não usei o .value.length (ou seja, o valor do comprimento)
    // e var == '' não funciona! Tem que ser igual a 0 msm!
    if (inicio.value.length == 0 || fim.value.length == 0 || passo.value.length == 0) {
        res.innerHTML = 'Impossível contar!'
        // window.alert('[ERRO] Faltam dados!')
    } else {
        res.innerHTML = 'Contando: <br>'
        let i = Number(inicio.value) // let é outra maneira de criar uma variável (subsitui o var)
        let f = Number(fim.value) // Faltou essas 4 linhas para o meu código funcionar! Gemini: O problema era que eu estava tentando 
        let p = Number(passo.value) // fazer a contagem com o valor do campo, mas não tinha transformado ele em número! Ele estava como 
                                    // string, e por isso não funcionava a contagem!
        if (p <= 0) {
            window.alert('Passo inválido! Considerando Passo como sendo 1!')
            p = 1 // Então é assim que faz o passo sendo = 1!!
        }
        
        if (i < f) { // isso é a contagem do menor para o maior
            for (let c = i; c <= f; c += p) { // c += p é a mesma coisa que c = c + p
                res.innerHTML += ` ${c} \u{1f449}` // Lembrando que += concatena (junta). Não soma! 
            }                                      // Faltou isso também para meu código funcionar!
        } else { 
            for (let c = i; c >= f; c -= p) { // isso é a contagem do menor para o maior 
                res.innerHTML += ` ${c} \u{1f449}`
            }
        }
        res.innerHTML += `\u{1f3c1}`
    }

    /* } else if (passo == 0) {
        window.alert('Passo inválido! Considerando Passo como sendo 1!')
    } else {
        for (inicio; inicio <= fim; inicio += passo) { // o problema é ou aqui
            res.innerHTML = `Contando... <br> ${console.log(inicio)}`
        }
        // res.innerHTML = `Contando... <br> ${console.log()}` // ou aqui!
    }*/
        
    

}
// Não consegui fazer a repetição (laço) e, portanto, o exercício.

// Lições do vídeo de resolução (LVR):

