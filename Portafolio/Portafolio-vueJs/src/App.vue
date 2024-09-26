<script setup>
  import NavBar from './components/NavBar.vue';
  import InformacionGral from './components/InformacionGral.vue';
  import Integrantes from './components/IntegrantesGrupo.vue';
  import HabilidadesComponent from './components/HabilidadesComponent.vue';
</script>

<template>
  <header>
    <!-- Barra de Navegacion -->
    <NavBar />
    <!-- Informacion General -->
    <InformacionGral />
  </header>
  <main>
    <section id="quienes somos">
      <h2 class="section-title">¿Quienes Somos?</h2>
    </section>
    <section id="miembros">
      <h2 class="section-title">Integrantes 💪</h2>
      <Integrantes />
    </section>
    <section id="proyectos ">
      <h2 class="section-title">Proyectos 💡</h2>
    </section>
    <section id="habilidades">
      <h2 class="section-title">Habilidades 📚</h2>
      <HabilidadesComponent />
    </section>
    <section id="intereses">
      <h2 class="section-title">Intereses</h2>
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
  border-bottom: 1px solid #ccc;
}
</style>
