<script setup>
import { ref } from 'vue';

const redsocial = ref([
    {id:1, nombre:'Linkedin', src:'/src/assets/linkedin_icon.svg', url:""},
    {id:2, nombre:'Instagram', src:'/src/assets/instagram_icon.svg', url:""},
    {id:3, nombre:'Facebook', src:'/src/assets/github_icon.svg', url:""},
    {id:4, nombre:'Curriculum Vitae',src:'/src/assets/cv_resume_icon.svg', url:""}

])
</script>

<template>
<section class="quienes-somos">
    <div class="card">
        <h1>Hello World</h1>
        <h2> Grupo de estudiantes de la Tecnicauta Universitaria en Programación - UTN</h2>
        <p> Hola, Bienvenido a nuestro portafolio de proyectos. Somos 5 estudiantes de la TUP aprendiendo sobre desarollo de aplicaciones web y móviles</p>
        <ul class="container-lista">
            <a v-for="nav in redsocial" :key="nav.nombre" href="nav.enlace" class="icon-redsocial"> {{ nav.nombre }}</a>
        </ul>
        <h3>Nuestro telefono es: +54 9 261-5522560</h3>
        <h4> Argentina </h4>
    </div>
</section>
</template>

<style scoped>
.container-lista{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    padding: 10px;
    background-color: rgba(92, 129, 231, 0.934);
}

.icon-redsocial{
    align-items: center;
    background-color: aliceblue;
    border-radius: 50%;
    padding: 2px;
    margin: 5px;
    box-shadow: 0 0 5px rgba(95, 124, 205, 0.934);
}

.icon-redsocial:hover{
    background-color: rgb(28, 41, 52);
    box-shadow: 0 0 5px rgba(251, 249, 249, 0.934);
}

h3{
    font-size: 1.2rem;
    font-weight: 600;
}

</style>