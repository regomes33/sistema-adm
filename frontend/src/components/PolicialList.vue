
<template>
  <div class="main-container">
    <div>
      <h1>Polciais Cadastrados</h1>
    </div>
    <div class="botaoCadastrar">
     <router-link :to="{name:'addpolicial'}"> <button type="button" class="btn btn-primary">Cadastrar Policial</button></router-link>
    </div>
    <table class="table table-striped">
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
          <td>{{ policial.id }}</td>
          <td>{{ policial.nome }}</td>
          <td>{{ policial.sobrenome }}</td>
          <td>{{ policial.rg_militar }}</td>
          <td>{{ policial.cpf }}</td>
          <td>{{ getPostoNome(policial.posto) }}</td>
          <td>{{ getGraduacaoDescricao(policial.graduacao) }}</td>
        <router-link :to ="{name:'/policialdetail', params:{ id: policial.id}}"> <button>Detalhes</button></router-link>
        
       
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
const endpoint = "http://localhost:8000/";
export default {
  name: "Policiais",

  data() {
    return {
      policiais: [],
      postos: [],
      graduacoes: [],
    };
  },

  mounted() {
    this.getPoliciais();
    this.getPostos();
    this.getGraduacoes();
  },

  methods: {
    getPoliciais() {
      axios.get("/api/policiais/").then((response) => {
        this.policiais = response.data;
      });
    },
   
    getPostos() {
      axios.get("/api/postos/").then((response) => {
        this.postos = response.data;
      });
    },

    getGraduacoes() {
      axios.get("/api/graduacoes/").then((response) => {
        this.graduacoes = response.data;
      });
    },

    getPostoNome(posto_id) {
      const posto = this.postos.find(p => p.id === posto_id);
      return posto ? posto.posto : "";
    },

    getGraduacaoDescricao(graduacao_id) {
      const graduacao = this.graduacoes.find(g => g.id === graduacao_id);
      return graduacao ? graduacao.graduacao : "";
      
    },
  },
  
};
</script>

<style scoped>
.botaoCadastrar {
text-align: right;
}
</style>

