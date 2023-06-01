//Arquivo Javascript para edição do mapa interativo

let areas = document.querySelectorAll('#mun_3549904, #mun_3502507, #mun_3508504, #mun_3554102, #mun_3524402');
let textIds = ['text3947', 'text3957', 'text4005', 'text3997', 'text4081'];

areas.forEach(function(area){
    area.addEventListener('mouseover', function(){
    area.style.fill = '#1B5161';

    textIds.forEach(function(textId) {
        const texto = document.getElementById(textId);
        if (texto) {
          texto.style.fill = '#ffffff';
        }
      });
    });
    area.addEventListener('mouseout', function(){
        area.style.fill = '#ffffff'
        textIds.forEach(function(textId) {
            const texto = document.getElementById(textId);
            if (texto) {
              texto.style.fill = '#000000';
            }
          });
        });
      });