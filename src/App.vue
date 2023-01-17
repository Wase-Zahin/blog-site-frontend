<template>
  <RouterView />
  <div>
    <!-- <router-link to="/blog_section">Blog</router-link> -->
    <header_bar></header_bar>
  </div>
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
