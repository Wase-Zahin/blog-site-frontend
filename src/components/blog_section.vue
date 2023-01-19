<template>
    <main>
        <h1><span>All Blogs</span></h1>
        <nav>
            <ul>
                <li>
                    <h3>Blog 1</h3>
                    <p>This is blog 1</p>
                </li>
                <li>
                    <h3>Blog 2</h3>
                    <p>This is blog 2</p>
                </li>
                <li>
                    <h3>Blog 3</h3>
                    <p>This is blog 3</p>
                </li>
            </ul>
        </nav>
    </main>
</template>

<script>
// import axios from 'axios';

export default {
  name: 'blog_section',
  data() {
    return {
      msg: 'Hello!',
    };
  },
  // methods: {
  //   getMessage() {
  //     const path = 'http://localhost:5000/ping';
  //     axios.get(path)
  //       .then((res) => {
  //         console.log(res);  
  //         this.msg = res.data.msg;
  //       })
  //       .catch((error) => {
  //         // eslint-disable-next-line
  //         console.error(error);
  //       });
  //   },
  // },
  // created() {
  //   this.getMessage();
  // }
};
</script> 