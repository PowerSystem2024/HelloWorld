<script setup>
  import NavBar from './components/NavBar.vue';
  import InformacionGral from './components/InformacionGral.vue';
  import Integrantes from './components/IntegrantesGrupo.vue';
  import HabilidadesComponent from './components/HabilidadesComponent.vue';
  import ProyectosComponent from './components/ProyectosComponent.vue';
</script>

<template>
  <header>
    <!-- Barra de Navegacion -->
    <NavBar />
    <!-- Informacion General -->
    <InformacionGral />
  </header>
  <main>
    <section id="miembros">
      <h2 class="section-title">Integrantes 💪</h2>
      <Integrantes />
    </section>
    <section id="proyectos ">
      <h2 class="section-title">Proyectos 💡</h2>
      <ProyectosComponent/>
    </section>
    <section id="habilidades">
      <h2 class="section-title">Habilidades 📚</h2>
      <HabilidadesComponent />
    </section>
  </main>
</template>

<style scoped>
/* Estilo para títulos */
.section-title {
  font-size: 2em;
  font-weight: bold;
  color: #f8f8f8;;
  text-align: center;
  margin: 20px 0;
  text-transform: uppercase;
  letter-spacing: 1px;
}

/* Opcional: Estilo para secciones */
section {
  padding: 20px;
  border-bottom: 3px solid #ccc;
}
</style>
