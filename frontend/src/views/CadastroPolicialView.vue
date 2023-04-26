
<template>
  <div class="main-container">
  <h1> Cadastro de Policiais</h1>
  <PolicialForm />
  </div>
</template>

<script>
import PolicialForm from "../components/PolicialForm.vue"
export default {
  name: "CadastroPolicialView",
  components:{
    PolicialForm,
  }
};
</script>

<style >
 .body{
  background-color: aliceblue;
 }
</style>