function carregar() {
    var msg = window.document.getElementById('msg')
    var img = document.getElementById('imagem')
    var data = new Date()
    // var hora = 13 // Para forçar a hora e testar o código!
    var hora = data.getHours()
    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora >= 0 && hora < 12) {
        // BOM DIA!!    
        img.src = 'foto_manha.png'
        document.body.style.background = '#5487b7' // Aqui usou o código hexa-decimal para pegar o 
    } else if (hora >= 12 && hora < 18) { // pigmento da cor de fundo!!!
        // BOA TARDE!!
        img.src = 'foto_tarde.png'
        document.body.style.background = '#fd9630'
    } else {
        // BOA NOITE!!
        img.src = 'foto_noite.png'
        document.body.style.background = '#08302f'
    }
}