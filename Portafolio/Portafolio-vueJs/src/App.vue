<script setup>
  import NavBar from './components/NavBar.vue';
  import InformacionGral from './components/InformacionGral.vue';
</script>

<template>
  <header>
    <!-- Barra de Navegacion -->
    <NavBar />
    <!-- Informacion General -->
     <InformacionGral />

  </header>
  <main>
    <section id="quienes somos"><h2>¿Quienes Somos?</h2></section>
    <section id="miembros"><h2>Miembros</h2></section>
    <section id="proyectos"><h2>Proyectos</h2></section>
    <section id="habilidades"><h2>Habilidades</h2></section>
    <section id="intereses"><h2>Intereses</h2></section>
  </main>
</template>

<style scoped>

</style>
