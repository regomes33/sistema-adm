<template>
    <div>
     <p>Editar Policial</p>
    </div>
    <div>
     <form id="policial-form" >
         <div class="input-container">
             <label for="nome">Nome do Policial</label>
             <input type="text" id="nome" name="nome" v-model="policial.nome" placeholder="Digite o nome">
         </div>
         <div class="input-container">
             <label for="sobrenome">Sobrenome do Policial</label>
             <input type="text" id="sobrenome" name="sobrenome" v-model="policial.sobrenome" placeholder="Digite o sobrenome">
         </div>
         <div class="input-container">
             <label for="rg_militar">RG Militar</label>
             <input type="number" id="rg_militar" name="rg_militar" v-model="policial.rg_militar" placeholder="Digite o RG">
         </div>
          <div class="input-container">
             <label for="cpf">CPF</label>
             <input type="text" id="cpf" name="cpf" v-model="policial.cpf" placeholder="Digite o CPF">
         </div>
          <div class="input-container">
             <label for="posto">Posto</label>
             <select name="posto" id="posto" v-model="policial.posto">
             <option value="">Selecione o Posto</option>
             </select>
         </div>
          <div class="input-container">
             <label for="graduacao">Graduação</label>
             <select name="graduacao" id="graduacao" v-model="policial.graduacao">
             <option value="">Selecione a Graduação</option>
             </select>
         </div>
         <button type="submit" class="btn btn-primary" @click="submitForm">Salvar Mudanças</button>
     </form>
    </div>
    <br/>
    <p>Edição dos Dados do Policial </p>
 </template>
 
 <script>
 import axios from 'axios'
 
 export default{
     name: "PolicialEdit",
 
     data(){
         return{
             policial:{},
             Posto:[],
             Graduacao:[]
 
         }
     },
     mounted(){
        this.getPolicial

     },
     methods:{
        getPolicial(){
            const policialID=this.$route.params.id 

            axios
                 .get(`/api/policiais/${policialID}/`)
                 .then(response=>{
                    this.policial=response.data
                 })
        },

       submitForm(){
        const policialID= this.$route.params.id

         axios
                .patch(`/api/policiais/${policialID}`,this.policial)
                .then(response=>{
                    this.$router.push('/list/policiais')
                })
                .catch(error=>{
                    console.log(JSON.stringify(error))
                })
            
       }
     }    
 
 }
 </script>
 
 <style scoped>
     #policial-form{
         max-width: 400px;
         margin: 0 auto;
 
 
     }
     .input-container{
         display: flex;
         flex-direction: column;
         margin-bottom: 20px;
     
     }
 
     label{
         font-weight: bold;
         color:black;
         padding: 5px 10px;
         border-left: 4px solid #fcba03;
     }
 
     input,select{
         padding: 5px 10px;
         width: 300px;
        
     }
     .btn-primary{
         border: 2px solid #222;
         padding: 10px;
         font-size: 16px;
         margin: 0 auto;  
     }
 
 </style>
