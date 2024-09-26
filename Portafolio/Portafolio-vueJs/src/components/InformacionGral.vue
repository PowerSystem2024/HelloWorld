<script setup>
import { ref } from 'vue';
const titulo = 'Hello World 🌎';
const descripcion = 'Grupo de estudiantes de la Tecnicatura Universitaria en Programación - UTN';
const presentacion = 'Hola, Bienvenido a nuestro portafolio de proyectos. Somos 5 estudiantes de la TUP aprendiendo sobre desarollo de aplicaciones web y móviles';
const residencia = 'Argentina';
const telefono = '+54 9 261-5522560';
const redsocial = ref([
    {id:1, nombre:'Linkedin', src:'/src/components/icons/linkedin_icon.svg', url:""},
    {id:2, nombre:'Instagram', src:'/src/components/icons/instagram_icon.svg', url:""},
    {id:3, nombre:'Facebook', src:'/src/components/icons/github_icon.svg', url:""},
    {id:4, nombre:'Curriculum Vitae',src:'/src/components/icons/cv_resume_icon.svg', url:""}

])
</script>

<template>
<section class="informacionGral">
    <div class="card">
        <h1>{{titulo}}</h1>
        <h2> {{ descripcion }}</h2>
        <p> {{ presentacion }}</p>
        <ul class="container-lista">
           <li v-for="red in redsocial" :key="red.id">
                <a href="red.url"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
           </li>
        </ul>
        <h3>Nuestro telefono es: {{ telefono }}</h3>
        <h4> {{ residencia }} </h4>
    </div>
</section>
</template>

<style scoped>
h1{
    font-size: 2.5rem;
    color: #ffffff;
    font-weight: bold;
}

p{
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: #fafaf9;
}

.card {
    background-color: #689F38;
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    text-align: center;
}

.container-lista{
    display: flex;
    justify-content: center;
   list-style: none;
   padding: 0;
   margin: 0;
   text-align: center;
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
    color:#f0f1ed ;
}

h2{
    color: #316870;
    font-weight: bold;
}

</style>