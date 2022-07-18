<template>
  <Banner />
  <PolicialList />
  
</template>

<script>
import Banner from "../components/Banner.vue";
import PolicialList from "../components/PolicialList.vue"
export default {
  name: "Home",
  components: {
    Banner,
    PolicialList,
  },
};
</script>