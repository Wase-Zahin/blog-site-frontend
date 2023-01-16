<template>
  <div>
    <router-link to="/blog-section">Blog</router-link>
    <header_bar></header_bar>

  </div>
  <router-view />

</template>

<script>
import header_bar from "./components/header_bar.vue"

export default {
  name: 'App',
  data() {
    return {
      msg: 'gbng',
    };
  },
  components: {
    header_bar,
  },
  methods: {

  },
};
</script>
