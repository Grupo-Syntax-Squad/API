//Arquivo Javascript para edição do mapa interativo

let areas = document.querySelectorAll('#mun_3549904, #mun_3502507, #mun_3508504, #mun_3554102, #mun_3524402');

areas.forEach(function(area){
    area.addEventListener('mouseover', function(){
    area.style.fill = '#1B5161'
    });
    area.addEventListener('mouseout', function(){
        area.style.fill = '#ffffff'
        })
    });
