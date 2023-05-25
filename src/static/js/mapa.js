//Arquivo Javasccript para edição do mapa interativo
const aparecidaArea = document.getElementById("aparecida");
const imagemaparecida = document.getElementById("imagemArea");
aparecidaArea.addEventListener("mouseover", function() {
imagemaparecida.innerHTML = '<img src="../static/mapas/aparecida.jpg" alt="Area - Aparecida" class="mapa2-img">';
});
aparecidaArea.addEventListener("mouseleave", function() {
imagemaparecida.innerHTML = '';
});

const caçapavaArea = document.getElementById("cacapava");
const imagemcaçapava = document.getElementById("imagemArea");
caçapavaArea.addEventListener("mouseover", function() {
imagemcaçapava.innerHTML = '<img src="../static/mapas/caçapava.jpg" alt="Area - Caçapava" class="mapa2-img">';
});
caçapavaArea.addEventListener("mouseleave", function() {
imagemcaçapava.innerHTML = '';
});

const jacareiArea = document.getElementById("jacarei");
const imagemjacarei = document.getElementById("imagemArea");
jacareiArea.addEventListener("mouseover", function() {
imagemjacarei.innerHTML = '<img src="../static/mapas/jacarei.jpg" alt="Area - Jacareí" class="mapa2-img">';
});
jacareiArea.addEventListener("mouseleave", function() {
imagemjacarei.innerHTML = '';
});

const sjcArea = document.getElementById("sjc");
const imagemsjc = document.getElementById("imagemArea");
sjcArea.addEventListener("mouseover", function() {
imagemsjc.innerHTML = '<img src="../static/mapas/saojose.jpg" alt="Area - São José Dos Campos" class="mapa2-img">';
});
sjcArea.addEventListener("mouseleave", function() {
imagemsjc.innerHTML = '';
});

const taubateArea = document.getElementById("taubate");
const imagemtaubate = document.getElementById("imagemArea");
taubateArea.addEventListener("mouseover", function() {
imagemtaubate.innerHTML = '<img src="../static/mapas/taubate.jpg" alt="Area - Taubaté" class="mapa2-img">';
});
taubateArea.addEventListener("mouseleave", function() {
imagemtaubate.innerHTML = '';
});