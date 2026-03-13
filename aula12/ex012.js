var agora = new Date()
var hora = agora.getHours() // ambos os comandos de cima são para mostrar a hora exata!!
console.log(`Agora são exatamente ${hora} horas`)
if (hora > 5 && hora <= 11) {
    console.log('Bom dia!') // dia = 6-11
} else if (hora >= 0 && hora <= 5) {
    console.log('Boa madrugada!') // opicional - madrugada = 0-5
} else if (hora > 11 && hora <= 17) { // tarde = 12-17
    console.log('Boa tarde')
} else {
    console.log('Boa noite!') // note = 18-23
}