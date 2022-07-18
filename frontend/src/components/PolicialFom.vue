<template>
   <div>
    <p>Componenente de mesagem</p>
   </div>
   <div>
    <form id="policial-form">
        <div class="input-container">
            <label for="nome">Nome do Policial</label>
            <input type="text" id="nome" name="nome" v-model="nome" placeholder="Digite o nome">
        </div>
        <div class="input-container">
            <label for="sobrenome">Sobrenome do Policial</label>
            <input type="text" id="sobrenome" name="sobrenome" v-model="nome" placeholder="Digite o sobrenome">
        </div>
        <div class="input-container">
            <label for="rg_militar">RG Militar</label>
            <input type="number" id="rg_militar" name="rg_militar" v-model="rg_militar" placeholder="Digite o RG">
        </div>
         <div class="input-container">
            <label for="cpf">CPF</label>
            <input type="text" id="cpf" name="cpf" v-model="cpf" placeholder="Digite o CPF">
        </div>
         <div class="input-container">
            <label for="posto">Posto</label>
            <select name="posto" id="posto" v-model="posto">
            <option value="">Selecione o Posto</option>
            </select>
        </div>
         <div class="input-container">
            <label for="graduacao">Graduação</label>
            <select name="graduacao" id="graduacao" v-model="graduacao">
            <option value="">Selecione a Graduação</option>
            </select>
        </div>
        <button type="submit" class="btn btn-primary">Cadastrar</button>
    </form>
   </div>
   <br/>
   <p>Cadastro de policial sistema </p>
</template>

<script>
export default{
    name: "PolicialForm"
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