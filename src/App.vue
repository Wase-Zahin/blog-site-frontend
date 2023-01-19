<template>
  <RouterView />
  <div>
    <!-- <router-link to="/blog_section">Blog</router-link> -->
    <!-- <header_bar></header_bar> -->
  </div>
</template>

<script>
// import header_bar from "./components/header_bar.vue"
// import login_page from "./components/login_page.vue";

export default {
  name: 'App',
  data() {
    return {
      msg: 'gbng',
    };
  },
  components: {
   // header_bar,
    // login_page
},
  methods: {

  },
};
</script>
