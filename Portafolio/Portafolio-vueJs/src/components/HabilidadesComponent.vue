<script setup>
import { ref } from 'vue';

const subtitulo1 = 'Frontend';
const frontLista = ref([
    { id: 1, nombre: 'HTML', src: '/src/components/icons/html.svg' },
    { id: 2, nombre: 'CSS', src: '/src/components/icons/css.svg' },
    { id: 3, nombre: 'JavaScript', src: '/src/components/icons/javascript.svg' },
    { id: 4, nombre: 'Vue.Js', src: '/src/components/icons/vuejs.svg' }
])
const subtitulo2 = 'Backend'
const backLista = ref([
    { id: 1, nombre: 'Java', src: '/src/components/icons/java.svg' },
    { id: 2, nombre: 'Python', src: '/src/components/icons/python.svg' },
    { id: 3, nombre: 'Node.js', src: '/src/components/icons/nodejs.svg' }
])
const subtitulo3 = 'Base de Datos'
const datosLista = ref([
    { id: 1, nombre: 'MySQL', src: '/src/components/icons/mysql.svg' }
])
const subtitulo4 = 'Control de Versiones'
const versionesLista = ref([
    { id: 1, nombre: 'Git', src: '/src/components/icons/git.svg' },
    { id: 2, nombre: 'GitHub', src: '/src/components/icons/github.svg' }
])
</script>

<template>
    <div class="stacks-container">
        <!-- Sección Frontend -->
        <section>
            <h2>{{ subtitulo1 }}</h2>
            <ul>
                <li v-for="front in frontLista" :key="front.id">
                    <img :src="front.src" alt="Icono de {{ front.nombre }}" class="front-img">
                    <div>
                        {{ front.nombre }}
                    </div>
                </li>
            </ul>
        </section>

        <!-- Sección Backend -->
        <section>
            <h2>{{ subtitulo2 }}</h2>
            <ul>
                <li v-for="back in backLista" :key="back.id">
                    <img :src="back.src" alt="Icono de {{ back.nombre }}" class="back-img">
                    <div>
                        {{ back.nombre }}
                    </div>
                </li>
            </ul>
        </section>

        <!-- Sección Bases de Datos y Control de Versiones (en una columna) -->
        <div class="combined-section">
            <!-- Sección Base de Datos -->
            <section>
                <h2>{{ subtitulo3 }}</h2>
                <ul>
                    <li v-for="datos in datosLista" :key="datos.id">
                        <img :src="datos.src" alt="Icono de {{ datos.nombre }}" class="datos-img">
                        <div>
                            {{ datos.nombre }}
                        </div>
                    </li>
                </ul>
            </section>

            <!-- Sección Control de Versiones -->
            <section>
                <h2>{{ subtitulo4 }}</h2>
                <ul>
                    <li v-for="versiones in versionesLista" :key="versiones.id">
                        <img :src="versiones.src" alt="Icono de {{ versiones.nombre }}" class="versiones-img">
                        <div>
                            {{ versiones.nombre }}
                        </div>
                    </li>
                </ul>
            </section>
        </div>
    </div>
</template>

<style scoped>
.stacks-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* Tres columnas */
    gap: 20px; /* Espacio entre columnas */
    margin: 20px 0;
}

/* Estilos generales */
h2 {
    text-align: center;
    color: #333;
    font-weight: bold;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    margin-bottom: 5px;
    padding: 10px;
    border-radius: 5px;
    text-align: center;
    background-color: #1976D2;
    color: #E3F2FD;
}

/* Sección combinada para Base de Datos y Control de Versiones */
.combined-section {
    display: flex;
    flex-direction: column; /* Coloca las secciones en una columna */
    gap: 20px; /* Espacio entre las secciones dentro de la columna */
}
</style>
