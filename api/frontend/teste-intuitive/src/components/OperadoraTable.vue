<script setup>
defineProps({
  operadora: Object,
});
</script>

<template>
  <div v-if="operadora" class="operadora-table">
    <h2>Dados da Operadora</h2>
    <table>
      <tr>
        <th>ID</th>
        <td>{{ operadora.id }}</td>
      </tr>
      <tr>
        <th>Registro ANS</th>
        <td>{{ operadora.reg_ans }}</td>
      </tr>
      <tr>
        <th>CNPJ</th>
        <td>{{ operadora.cnpj }}</td>
      </tr>
      <tr>
        <th>Razão Social</th>
        <td>{{ operadora.razao_social }}</td>
      </tr>
      <tr>
        <th>Nome Fantasia</th>
        <td>{{ operadora.nome_fantasia }}</td>
      </tr>
      <tr>
        <th>Modalidade</th>
        <td>{{ operadora.modalidade }}</td>
      </tr>
      <tr>
        <th>Logradouro</th>
        <td>{{ operadora.logradouro }}</td>
      </tr>
      <tr>
        <th>Número</th>
        <td>{{ operadora.numero }}</td>
      </tr>
      <tr>
        <th>Complemento</th>
        <td>{{ operadora.complemento }}</td>
      </tr>
      <tr>
        <th>Bairro</th>
        <td>{{ operadora.bairro }}</td>
      </tr>
      <tr>
        <th>Cidade</th>
        <td>{{ operadora.cidade }}</td>
      </tr>
      <tr>
        <th>UF</th>
        <td>{{ operadora.uf }}</td>
      </tr>
      <tr>
        <th>CEP</th>
        <td>{{ operadora.cep }}</td>
      </tr>
      <tr>
        <th>DDD</th>
        <td>{{ operadora.ddd }}</td>
      </tr>
      <tr>
        <th>Telefone</th>
        <td>{{ operadora.telefone }}</td>
      </tr>
      <tr>
        <th>Fax</th>
        <td>{{ operadora.fax }}</td>
      </tr>
      <tr>
        <th>E-mail</th>
        <td>{{ operadora.endereco_eletronico }}</td>
      </tr>
      <tr>
        <th>Representante</th>
        <td>{{ operadora.representante }}</td>
      </tr>
      <tr>
        <th>Cargo do Representante</th>
        <td>{{ operadora.cargo_representante }}</td>
      </tr>
      <tr>
        <th>Região de Comercialização</th>
        <td>{{ operadora.regiao_comecializacao }}</td>
      </tr>
      <tr>
        <th>Data de Registro</th>
        <td>{{ operadora.data_registro }}</td>
      </tr>
    </table>
  </div>
</template>

<style scoped>
.operadora-table table {
  width: 100%;
  border-collapse: collapse;
}

.operadora-table th,
.operadora-table td {
  border: 1px solid #ddd;
  padding: 8px;
  color: white;
}

.operadora-table th {
  background-color: #141212;
  text-align: left;
  color: white;
}
</style>
