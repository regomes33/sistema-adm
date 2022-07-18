<template>
  <div class="main-container">
    <div>
      <h1>Lista de Escalas Extraordinárias</h1>
    </div>
    <table class="table">
      <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col">Nome</th>
          <th scope="col">Sobrenome</th>
          <th scope="col">RG Militar</th>
          <th scope="col">CPF</th>
          <th scope="col">POSTO</th>
          <th scope="col">GRADUAÇÃO</th>
        
        </tr>
      </thead>
      <tbody>
        <tr v-for="policial in policiais" :key="policial.id">
        <td>{{policial.id}}</td>
        <td>{{policial.nome}}</td>
        <td>{{policial.sobrenome}}</td>
        <td>{{policial.rg_militar}}</td>
        <td>{{policial.cpf}}</td>
        <td>{{policial.posto}}</td>
        <td>{{policial.graduacao}}</td>
        </tr>
      </tbody>
    </table>
  </div>
  
</template>

<script>

import axios from 'axios'
const endpoint='http://localhost:8000/'
export default {
  name: "PolicialList",

  data() {
    return {
      policiais: [],
    };
  },
  
    mounted(){
        axios.get(endpoint + "api/policial/")
        .then((response)=> {
            this.policiais=response.data
        });
    }
  }
  

</script>