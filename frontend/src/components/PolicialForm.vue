<template>
  <div>
    <p>Componenente de mesagem</p>
  </div>
  <div>
    <form id="policial-form" @submit.prevent>
      <div class="input-container">
        <label for="nome">Nome do Policial</label>
        <input
          type="text"
          id="nome"
          name="nome"
          v-model="policial.nome"
          placeholder="Digite o nome"
        />
      </div>
      <div class="input-container">
        <label for="sobrenome">Sobrenome do Policial</label>
        <input
          type="text"
          id="sobrenome"
          name="sobrenome"
          v-model="policial.sobrenome"
          placeholder="Digite o sobrenome"
        />
      </div>
      <div class="input-container">
        <label for="rg_militar">RG Militar</label>
        <input
          type="text"
          id="rg_militar"
          name="rg_militar"
          v-model="policial.rg_militar"
          placeholder="Digite o RG"
        />
        <div v-if="rg_militarError" class="error">{{ rg_militarError }}</div>
      </div>
      <div class="input-container">
        <label for="cpf">CPF</label>
        <input
          type="text"
          id="cpf"
          name="cpf"
          v-model="policial.cpf"
          placeholder="Digite o CPF"
        />
        <div v-if="cpfError" class="error">{{ cpfError }}</div>
      </div>

      <div class="input-container">
        <label for="posto">Escolha o Posto</label>
        <select name="posto" id="posto" v-model="policial.posto.id">
          <option v-for="posto in postos" :key="posto.id" :value="posto.id">
            {{ posto.posto }}
          </option>
        </select>
      </div>

      <div class="input-container">
        <label for="graduacao">Graduação</label>
        <select name="graduacao" id="graduacao" v-model="policial.graduacao.id">
          <option
            v-for="graduacao in graduacoes"
            :key="graduacao.id"
            :value="graduacao.id"
          >
            {{ graduacao.graduacao }}
          </option>
        </select>
      </div>
      <button type="submit" class="btn btn-primary" @click="submitForm">
        Cadastrar
      </button>
    </form>
  </div>
  <br />

  <p>Cadastro de policial sistema</p>
</template>

<script>
import axios from "axios";

export default {
  name: "PolicialForm",

  data() {
    return {
      policial: {
        posto: {
          id: null,
          nome: "",
        },
        graduacao: {
          id: null,
          nome: "",
        },
      },
      postos: [],
      graduacoes: [],
      // Variável para armazenar os dados inseridos pelo usuário
      userData: {
        nome: "",
        sobrenome: "",
        rg_militar: "",
        cpf: "",
        postoId: null,
        graduacaoId: null,
      },
      // Variável para exibir mensagens de erro
      errorMessage: "",
      cpfError: "",
      rg_militarError: "",
    };
  },
  async mounted() {
    this.getPostos();
    this.getGraduacoes();
  },
  methods: {
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
    checkIfExists(campo, valor) {
      axios.get(`/api/policiais/?${campo}=${valor}`).then((response) => {
        if (response.data.length > 0) {
          if (campo === "cpf") {
            this.cpfError = "CPF já cadastrado";
          } else {
            this.rg_militarError = "RG já cadastrado";
          }
        }
      });
    },
    submitForm() {
      this.cpfError = "";
      this.rg_militarError = "";

      this.checkIfExists("cpf", this.policial.cpf);
      this.checkIfExists("rg_militar", this.policial.rg_militar);

      if (!this.cpfError && !this.rg_militarError) {
        axios
          .post("/api/policiais/", {
            nome: this.policial.nome,
            sobrenome: this.policial.sobrenome,
            rg_militar: this.policial.rg_militar,
            cpf: this.policial.cpf,
            posto: this.policial.posto.id,
            graduacao: this.policial.graduacao.id,
          })
          .then(() => {
            this.policial = {
              nome: "",
              sobrenome: "",
              rg_militar: "",
              cpf: "",
              posto: {
                id: null,
                nome: "",
              },
              graduacao: {
                id: null,
                nome: "",
              },
            };
          })
          .then((response) => {
          this.$router.push("/list/policiais");
        })
          .catch((error) => {
            if (error.response.status === 400) {
              // Se o erro for de validação, armazena os dados inseridos pelo usuário
              this.userData.nome = this.policial.nome;
              this.userData.sobrenome = this.policial.sobrenome;
              this.userData.rg_militar = this.policial.rg_militar;
              this.userData.cpf = this.policial.cpf;
              this.userData.postoId = this.policial.posto.id;
              this.userData.graduacaoId = this.policial.graduacao.id;
              console.log("sistema nao esta segurando o usuario");
              this.errorMessage = error.response.data.message;
            } else {
              console.error(error);
            }
            
          });
          
      }
      
    },
  },
};
</script>


<style scoped>
#policial-form {
  max-width: 400px;
  margin: 0 auto;
}
.input-container {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

label {
  font-weight: bold;
  color: black;
  padding: 5px 10px;
  border-left: 4px solid #fcba03;
}

input,
select {
  padding: 5px 10px;
  width: 300px;
}
.btn-primary {
  border: 2px solid #222;
  padding: 10px;
  font-size: 16px;
  margin: 0 auto;
}
</style>