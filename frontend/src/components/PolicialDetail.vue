<template>
    <div >
        <div >
            <h1>{{policial.nome}}</h1>
                <h1>{{policial.sobrenome}}</h1>
            terra
            
        </div>
    </div>
</template>

<script>
import axios from 'axios'


export default {
    name:'Policial',

    data(){
        return{
            policial:{}

        }
    },
    mounted(){
        this.getPolicial()
    },
    methods:{
        getPolicial(){
            const policialID=this.$route.params.id 

            axios
                 .get(`/api/policiais/${policialID}/`)
                 .then(response=>{
                    this.policial=response.data
                 })
        }
    }
   
}
</script>
