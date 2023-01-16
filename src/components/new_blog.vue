<template>
    <form>
        <input type="text" placeholder=" username"/>
        <input type="text" placeholder=" title"/>
        <textarea placeholder=" content" rows="15" cols="33"></textarea>
    </form>
</template>

<script>

export default {
  name: 'new_blog',
  data() {
    return {
      msg: 'Hello!',
    };
  },
};
</script> 