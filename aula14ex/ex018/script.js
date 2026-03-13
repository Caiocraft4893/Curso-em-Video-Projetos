function gerar() {
    var num = document.getElementById('num')
    var res = document.getElementById('res')
    var tabuada = document.getElementById('sel')
    if (num.value.length == 0) { 
        alert('Por favor, digite um número!')
    } else {
        var n = Number(num.value)
        if (n == 0) {
            alert('Qualquer número vezes 0 = 0!')
        } else {
            tabuada.innerHTML = '' // Gemini ajudou
            for (var c = 1; c <= 10; c += 1) { // Faz nessa estrutura: for (var c = x; lalala; lalala) que é sucesso!  E essa fiz sozinho!
                    var item = document.createElement('option') // Gemini ajudou - isso cria um novo elemnento de opção.
                    item.text = `${n} x ${c} = ${n*c}` // Gemini ajudou - isso define o texto que aparecerá para o usuário
                    item.value = `tab${c}` // Gemini ajudou - isso define o valor interno (útil para formulários) (opicional)
                    tabuada.appendChild(item) // Gemini ajudou - isso adiciona a opção dentro do select
                }                                               
        }
    }
}
 
/* Depois de muita pesquisa e perguntas ao Gemini, consegui fazer o exercício!
* Aprendi que para criar o campo da tabuada, é preciso colocar uma <option> dentro 
de uma <select>, dentro de um <form> (quanto coisa, hein!).
* Também que variável.innerHTML = '' limpa o conteúdo do campo, 
a função .text define o texto que aparecerá para o usuário, 
a função .value define o valor interno da variável (reaprendi) e a
variável.appendChild(item) adiciona um item dentro do campo.
* Gemini é uma boa IA para auxiliar no aprendizado de programção (especificamente programação!)
*/

