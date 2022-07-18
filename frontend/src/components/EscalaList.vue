<template>
    <div class="main-container">
    <div>
      <h1>Lista de Escalas Extraordinárias</h1>
    </div>
    <table class="table">
      <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col">VTR</th>
          <th scope="col">DIA/MÊS</th>
          <th scope="col">SEMANA</th>
          <th scope="col">HORÁRIO</th>
          <th scope="col">HORAS</th>
          <th scope="col">CPF</th>
          <th scope="col">RG</th>
          <th scope="col">NOME</th>
          <th scope="col">ASSINATURA</th>
          <th scope="col">RAI</th>
        </tr>
      </thead>
      <tbody>
        <!-- <tr v-for="policial in policiais" :key="policial.id">
        <td>{{policial.nome}}</td>
        <td>{{policial.sobrenome}}</td>
        </tr> -->
      </tbody>
    </table>
  </div>
  
  <div class="main-container">
    <h1>Lista das Escalas Ordinárias</h1>
    <table class="table">
      <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col">First</th>
          <th scope="col">Last</th>
          <th scope="col">Handle</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">1</th>
          <td>Mark</td>
          <td>Otto</td>
          <td>@mdo</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Jacob</td>
          <td>Thornton</td>
          <td>@fat</td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td>Larry</td>
          <td>the Bird</td>
          <td>@twitter</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
// import { defineComponent } from '@vue/composition-api'

export default {
    name :"EscalaList",
        
    
}
</script>
