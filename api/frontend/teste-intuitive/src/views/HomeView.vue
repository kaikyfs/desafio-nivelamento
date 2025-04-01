<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { getOperadoras } from '@/services/operadoras.js';
import OperadoraTable from '@/components/OperadoraTable.vue'; // Importando o componente

const searchQuery = ref('');
const router = useRouter();
const operadora = ref(null);
const errorMessage = ref(null);

const fetchOperadora = async () => {
    errorMessage.value = null; // Limpa a mensagem de erro antes de buscar
  try {
    const operadoras = await getOperadoras();

    if (!Array.isArray(operadoras)) {
      throw new Error('A resposta do servidor não é uma lista válida de operadoras.');
    }

    const operadoraEncontrada = operadoras.find(
      (operadora) =>
        operadora?.nome_fantasia?.toLowerCase() === searchQuery.value?.toLowerCase()
    );

    if (operadoraEncontrada) {
      operadora.value = operadoraEncontrada;
    } else {
      errorMessage.value = 'Operadora não encontrada';
      operadora.value = null;
    }
  } catch (error) {
    console.error('Erro ao buscar operadora:', error);
    errorMessage.value = 'Erro ao buscar operadora. Tente novamente mais tarde.';
  }
};
</script>

<template>
  <div class="home-view">
    <h1>Buscar Operadora</h1>
    <div class="search-bar">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Digite o nome da operadora"
        aria-label="Buscar operadora pelo nome"
      />
      <button :disable="!searchQuery" @click="fetchOperadora">Pesquisar</button>
    </div>

    <div v-if="errorMessage" class="error-message">
      {{ errorMessage }}
    </div>
    <OperadoraTable v-if="operadora" :operadora="operadora" />
  </div>
</template>

<style scoped>
.home-view {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  margin-bottom: 70vh;
  margin-right: 50vh;
}

.search-bar {
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
}

.search-bar input {
  flex: 1;
  padding: 10px;
  font-size: 16px;
  width: 50vh;
}

.search-bar button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

.error-message {
  color: red;
  margin-bottom: 20px;
}
</style>
