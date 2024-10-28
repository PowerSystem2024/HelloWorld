<script setup>
import python from "/src/components/icons/python.svg";
import javascript from "/src/components/icons/javascript.svg";
import html from "/src/components/icons/html.svg";
import css from "/src/components/icons/css.svg";
import sql from "/src/components/icons/sql.svg";
import java from "/src/components/icons/java.svg";
import react from "/src/components/icons/react.svg";
import vue from "/src/components/icons/vue.svg";
import git from "/src/components/icons/git.svg";
import vs from "/src/components/icons/vsc.svg";
import español from "/src/components/icons/argentina.svg";
import ingles from "/src/components/icons/eeuu.png";
import { ref } from 'vue';

var habilidades = ref([
    {
        categoria: "Lenguaje de Programacion",
        skills: [
            {
                nombre: "JavaScript",
                nivel: "Intermedio",
                icono: javascript
            },
            {
                nombre: "Python",
                nivel: "Intermedio",
                icono: python 
            },
            {
                nombre: "HTML",
                nivel: "Intermedio",
                icono: html
            },
            {
                nombre: "CSS",
                nivel: "Intermedio",
                icono: css
            },
            {
                nombre: "SQL",
                nivel: "Intermedio",
                icono: sql
            },
            {
                nombre: "Java",
                nivel: "Intermedio",
                icono: java
            }
        ]
    },
    {
        categoria: "Frameworks y Librerias",
        skills: [
            {
                nombre: "React",
                nivel: "Intermedio",
                icono: react
            },
            {
                nombre: "Vue",
                nivel: "Intermedio",
                icono: vue
            },
        ]
    },
    {
        categoria: "Herramientas y Software",
        skills: [
            {
                nombre: "Git",
                nivel: "Avanzado",
                icono: git
            },
            {
                nombre: "Visual Studio Code",
                nivel: "Avanzado",
                icono: vs
            }
        ]
    },
    {
        categoria: "Idiomas",
        skills: [
            {
                nombre: "Español",
                nivel: "Nativo",
                icono: español
            },
            {
                nombre: "Inglés",
                nivel: "Intermedio",
                icono: ingles
            }
        ]
    }
]);

console.log('Habilidades Component Loaded');
console.log(habilidades.value);
</script>

<template>
    <div class="skills-contenedor">
        <div v-for="categoria in habilidades" :key="categoria.categoria" class="skills-categoria">
            <h3>{{ categoria.categoria }}</h3>
            <ul class="skills">
                <li v-for="skill in categoria.skills" :key="skill.nombre" class="skill">
                    <img :src="skill.icono" :alt="skill.nombre">
                    <span>{{ skill.nombre }}: {{ skill.nivel }}</span>
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
.skills-contenedor {
    padding: 2rem;
    max-width: 1200px; /* Limitar el ancho para mejor visualización */
    margin: 0 auto; /* Centrar el contenedor */
}

.skills-categoria {
    margin-bottom: 30px; /* Mayor espacio entre categorías */
    border-bottom: 1px solid #8bc34a; /* Línea divisoria para separación visual */
    padding-bottom: 20px; /* Espacio interno debajo del título */
}

.skills-categoria h3 {
    display: flex;
    justify-content: center;
    margin-bottom: 10px;
    font-size: 1.8em; /* Aumentar el tamaño del título */
    color: #8bc34a; /* Color del texto */
    font-weight: bold;
    position: relative; /* Para usar un pseudo-elemento */
}

/* Línea decorativa debajo del título */


.skills {
    display: flex;
    justify-content: center; /* Centrar */
    flex-wrap: wrap;
    gap: 15px; /* Espacio entre los ítems */
}

.skill {
    display: flex;
    justify-content: center;
    align-items: center; /* Usar align-items para centrar verticalmente */
    gap: 10px;
    padding: 1em; /* Mayor espacio interno */
    border-radius: 8px;
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1); /* Sombra más suave */
    background-color: #f8f8f8; /* Fondo claro para las habilidades */
    transition: background-color 0.3s ease, transform 0.3s ease; /* Suavizar transiciones */
    flex: 1 1 calc(25% - 20px); /* Espacio adaptable con margen */
    max-width: 220px; /* Ancho máximo para cada habilidad */
}

.skill:hover {
    background-color: #f1f1f1; /* Fondo más claro en hover */
    transform: scale(1.05); /* Aumentar ligeramente el tamaño */
}

.skill img {
    width: 40px; /* Tamaño del icono */
    height: 40px; /* Tamaño del icono */
}

.skill span {
    font-size: 1.1em; /* Tamaño de texto ligeramente mayor */
    color: #333; /* Color del texto */
    font-weight: 500; /* Peso de fuente medio */
}

/* Responsividad */
@media (max-width: 768px) {
    .skills-categoria h3 {
        justify-content: center; /* Centrar el título en dispositivos más pequeños */
    }

    .skills {
        justify-content: center; /* Centrar los elementos en móviles */
    }

    .skill {
        flex: 1 1 calc(50% - 10px); /* Dos elementos por fila en móviles */
    }
}

@media (max-width: 480px) {
    .skill {
        flex: 1 1 100%; /* Un elemento por fila en pantallas muy pequeñas */
        max-width: none; /* Sin límite de ancho */
    }
}

</style>

