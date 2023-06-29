// ACOMODAR BARRA SUPERIOR
const supBar = document.querySelector('.sup_bar');

// Cambiar opacidad con Scroll
window.addEventListener('scroll', () => {
	if (window.scrollY > 0) {
		supBar.classList.add('transparent');
	} else {
		supBar.classList.remove('transparent');
	}
});

//para que el supbar reaccione al mouse
supBar.addEventListener('mouseover', () => {
	supBar.classList.remove('transparent');
});

supBar.addEventListener('mouseout', () => {
	supBar.classList.add('transparent');
});

//acomomodar el contenido principal
let supbarHeight = supBar.offsetHeight;
const mainContent = document.querySelector('.main_content');
mainContent.style.paddingTop = `${supbarHeight + 20}px`;


///////////PONER BOTON VERDE A LAS CANCIONES//////////////////////////

var music_card = document.querySelectorAll('.music_card');

const createButton = card => {
	const button = document.createElement('button');
	button.innerHTML = '<i class="fa-solid fa-play"></i>';
	card.appendChild(button);
	button.style.display = 'none';
	button.classList.add('btn_play');
	card.addEventListener('mouseover', () => {
		button.style.display = 'block';
	});
	card.addEventListener('mouseout', () => {
		button.style.display = 'none';
	});
};
music_card.forEach(card => {
	createButton(card);
});



////////////////////////////PARA SUBIR CANCION/////////////////////////////////

//ACTUALIZAR IMAGEN
const fileInputImg = document.getElementById('imgFile');
const imagePreview = document.getElementById('img_preview');
fileInputImg.addEventListener('change', function (event) {
	const selectedImage = event.target.files[0];
	if (selectedImage) {
		const reader = new FileReader();
		reader.onload = function (event) {
			imagePreview.src = event.target.result;
		}
		reader.readAsDataURL(selectedImage);
	}
});

//ACTUALIZAR ARCHIVO DE AUDIO
const fileInputMp3 = document.getElementById('mp3Files');
const audioPlayer = document.getElementById('mp3_preview');
fileInputMp3.addEventListener('change', function (event) {
	const selectedAudio = event.target.files[0];
	if (selectedAudio) {
		const audioURL = URL.createObjectURL(selectedAudio);
		audioPlayer.src = audioURL;
	}
});

// ACTUALIZAR NOMBRE CANCION
const textSongname = document.getElementById('song_name');
const labelOutputSong = document.getElementById('Songname_preview');
textSongname.addEventListener('input', function (event) {
	const texto = event.target.value;
	labelOutputSong.textContent = texto;
});

//ACTUALIZAR AUTOR
const textInputAutor = document.getElementById('Autor_name');
const labelOutputAutor = document.getElementById('autor_preview');
textInputAutor.addEventListener('input', function (event) {
	const texto = event.target.value;
	labelOutputAutor.textContent = texto;
});


//PARA ACTIVAR O DESACTIVAR AGREGAR MAS GENEROS
function checkOption(value) {
	var otherOption = document.getElementById("otherOption");
	var enableCheckbox = document.getElementById("enableOtherOption");

	if (value === "other") {
		otherOption.disabled = false;
		enableCheckbox.disabled = false;
	} else {
		otherOption.disabled = true;
		enableCheckbox.checked = false;
	}
}

function toggleOption() {
	var list_generos = document.getElementById("list_generos");
	var otherOption = document.getElementById("other_Option");
	var enableCheckbox = document.getElementById("enableOtherOption");

	if (enableCheckbox.checked) {
		list_generos.disabled = true;
		otherOption.style = "display: inline";
	} else {
		list_generos.disabled = false;
		otherOption.style = "display: none;";
		otherOption.value = "";
	}
}

//ACTIVAR O DESACTIVAR EL BOTON SUBIR CANCION
var boton = document.getElementById("btn_subir");
function activarSubir() {
	if (fileInputMp3.files.length > 0 && textInputAutor.value.trim() !== "" && textSongname.value.trim() !== "") {
		boton.disabled = false;
	} else {
		boton.disabled = true;
	}
}


//////////////////////PARA EDITAR CANCIONES///////////////////////////
function expandirDiv(){
	var camposAdicionales = document.getElementById("camposAdicionales");
	if(camposAdicionales.style.display == "none"){
		camposAdicionales.style.display = "block";
	}else{
		camposAdicionales.style.display = "none";
	}
}