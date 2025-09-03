// Cada vez que se haga scroll
document.addEventListener("scroll", () => {

    // 1. Definimos la función personalizada
    //function animarElementosAlHacerScroll() {
    // Seleccionamos todos los párrafos y subtítulos
    //const elements = document.querySelectorAll(".parrafo, .subtitulo, .subtitulo2");

    // Seleccionamos todos los parrafors, subtitulos y subtitulos2
    // querySelectorAll para escoger todas las clases con .parrafo, .subitutilo y .subtitulo2
    // Y se guarda dentro de la variqable elements como una node list 
    const elements = document.querySelectorAll(".parrafo, .subtitulo, .subtitulo2, .subtitulo3, .subtitulo4");

    // Para cada elemento de la constante elements lo almacenamos en la variable "el" 
    // que representa cada elemento de la node list (parrafo, subitutilo, ect)
    // Se recorre cada uno de los elementos usando forEach
    //  ForEach itera los elementos en cada grilla
    elements.forEach(el => {

      // Obtiene la distancia desde la parte superior del elemento hasta la parte superior de la ventana (viewport).
      const position = el.getBoundingClientRect().top;
      // Window.innerHeight es la altura visible de la ventana 
      // Se evalúa si la posición del elemento es menor al alto total de la ventana del navegador (window.innerHeight) menos 100 píxeles.
      if (position < window.innerHeight - 100) {
        el.classList.add("visible");
      }
    });
  });

// Seleccionamos todos los elementos con la clase "boton-compra"
const botones = document.querySelectorAll(".boton-compra");

// Recorremos cada uno de los botones encontrados
botones.forEach(boton => {
  
  // Agregamos un evento al hacer clic sobre cada botón
  boton.addEventListener("click", (e) => {
    
    // Previene que el enlace se abra automáticamente al hacer clic
    e.preventDefault();

    // Mostramos un cuadro de confirmación al usuario
    const respuesta = confirm("Vas a salir de esta página. ¿Quieres continuar?");

    // Si el usuario hace clic en "Aceptar"
    if (respuesta) {
      // Se abre el enlace en una nueva pestaña del navegador
      window.open(boton.href, '_blank');
    } else {
      // Si el usuario hace clic en "Cancelar", no se hace nada
      // El usuario permanece en la página actual
    }
  });


});

document.addEventListener("DOMContentLoaded", () => {
  // Selecciona las imágenes dentro del carrusel
  const images = document.querySelectorAll("#galeriaCarrusel img");

  // Crea el lightbox
  const lightbox = document.createElement("div");
  // Pone la caja en un lugar fijo
  lightbox.style.position = "fixed";
  // Pega la caja arriba y a la izquierda
  lightbox.style.top = 0;
  lightbox.style.left = 0;
  // Hace que la caja ocupe el 100% de la pantalla
  lightbox.style.width = "100%";
  lightbox.style.height = "100%";
  // Crea un color negro transparente dentro de la caja
  lightbox.style.backgroundColor = "rgba(0, 0, 0, 0.8)";
  // Oculta la caja 
  lightbox.style.display = "none";
  // Ajusta el contenido de la caja al centro y medio
  lightbox.style.justifyContent = "center";
  lightbox.style.alignItems = "center";
  // Cambia la apariencia del cursor cada vez que se haga encima de la imagen
  lightbox.style.cursor = "pointer";
  // z-index es una propiedad que define que tan encima se muestra algo en una pagina
  lightbox.style.zIndex = "9999"; // Asegúrate de que esté por encima de todo
  // Agrega la caja a la pagina para que podamos mostrarla cuandon queramos 
  document.body.appendChild(lightbox);

  // Crea la etiqueta imagen para que se pueda agregar en la caja 
  const img = document.createElement("img");
  // Limita la imagen al 90% de la pantalla
  img.style.maxWidth = "90%";
  img.style.maxHeight = "90%";
  // Pone la imagen dentro de la caja oscura que creamos
  lightbox.appendChild(img);

  // Mostrar lightbox al hacer clic en una imagen
  images.forEach(image => {
    image.style.cursor = "pointer";
    // Al hacer click en la imagen ejecuta lo que hay dentro de la funcion
    image.addEventListener("click", () => {
      // Pon en la imagen grande la misma foto que la persona clickeo
      img.src = image.src;
      lightbox.style.display = "flex";
    });
  });

  // Cerrar el lightbox al hacer clic en él
  lightbox.addEventListener("click", () => {
    lightbox.style.display = "none";
  });
});

function encender() {
  const bonfire = document.getElementById("bonfire");
  const overlay = document.getElementById("overlay");

  bonfire.classList.remove("darkness");       // Quitar filtro de la hoguera
  bonfire.src = bonfire.src;                  // Reiniciar el gif
  overlay.style.opacity = "0";                // Quitar la oscuridad del fondo
}

function apagar() {
  const bonfire = document.getElementById("bonfire");
  const overlay = document.getElementById("overlay");

  bonfire.classList.add("darkness");          // Agregar filtro a la hoguera
  overlay.style.opacity = "1";                // Oscurecer fondo
}

