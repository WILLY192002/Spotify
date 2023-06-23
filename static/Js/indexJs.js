const supBar = document.querySelector('.sup_bar');

// Cambiar opacidad con Scroll
window.addEventListener('scroll', () => {
	if (window.scrollY > 0) {
		supBar.classList.add('transparent');
	} else {
		supBar.classList.remove('transparent');
	}
});

supBar.addEventListener('mouseover', () => {
	supBar.classList.remove('transparent');
});

supBar.addEventListener('mouseout', () => {
	supBar.classList.add('transparent');
});

// Nueva variable para almacenar altura del Topbar
let supbarHeight = supBar.offsetHeight;
// Añadimos un paddingTop basado en la altura al main-content o el contenido principal
const mainContent = document.querySelector('.main_content');
mainContent.style.paddingTop = `${supbarHeight + 20}px`;

const container_music_card = document.querySelectorAll(
	'.music_card'
);

// Función que se va a repetir
const createButton = card => {
	// Crear el botón
	const button = document.createElement('button');
	button.innerHTML = '<i class="fa-solid fa-play"></i>';

	// Agregar el botón al elemento hijo
	card.appendChild(button);

	// Ocultar el botón inicialmente
	button.style.display = 'none';
	button.classList.add('btn_play');

	// Agregamos un evento de hover a este elemento
	// Se necesita cuando el mouse entra y cuando sale
	card.addEventListener('mouseover', () => {
		button.style.display = 'block';
	});

	card.addEventListener('mouseout', () => {
		button.style.display = 'none';
	});
};

container_music_card.forEach(card => {
	createButton(card);
});