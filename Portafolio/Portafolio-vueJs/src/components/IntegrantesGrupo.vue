<script setup>
import { ref } from 'vue';

const listaMiembros = ref([
    { id: 1, nombre: 'Rosario Danna Martinez Baez', edad: '29 años', origen: 'Ciudad de Mendoza', src: '/src/components/icons/danna.png' },
    { id: 2, nombre: 'Juan Bisaguirre', edad: '33 años', origen: 'Ciudad de Mendoza', src: '/src/components/icons/Juanb.jpg' },
    { id: 3, nombre: 'Julieta Aguilera', edad: '20 años', origen: 'San Rafael, Mendoza', src: '/src/components/icons/juli.jpg' }, 
    { id: 4, nombre: 'Carlos Ariel Diaz Cattoni', edad: '27 años', origen: 'Las Heras, Mendoza', src: '/src/components/icons/carlos.jpg' }
]);
</script>

<template>
  <section class="Integrantes">
    <div class="card">
      <ul>
        <li v-for="miembro in listaMiembros" :key="miembro.id">
          <img :src="miembro.src" alt="Foto de {{ miembro.nombre }}" class="miembro-img">
          <div class="info">
            <strong class="nombre">{{ miembro.nombre }}</strong> <br>
           {{ miembro.edad }} <br>
           {{ miembro.origen }}
          </div>
        </li>
      </ul>
    </div>
  </section>
</template>

<style scoped>
li {
  list-style: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; /* Centra horizontalmente */
  margin-bottom: 15px;
  font-size: larger;
}

.miembro-img {
  width: 150px;
  height: 150px;
  margin-right: 20px; /* Aumenta el margen para separar imagen y texto */
  border-radius: 50%;
  object-fit: cover;
}

.card {
  padding: 20px;
  border-radius: 8px;
}

.info {
  text-align: center; /* Centra el texto dentro del div */
}

.nombre {
  font-weight: bold;
  font-size: 1.5em; /* Aumenta el tamaño de la fuente del nombre */
}
</style>
