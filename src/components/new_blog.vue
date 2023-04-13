<template>
    <form ref="formFields" class="newBlog" @submit="onSubmit">
        <h3 class="create_blog_header">Create a new Blog!</h3>
        <input 
        v-model="username"
        placeholder="Username" 
        name="username" 
        id="username"
        required
        />
        <input 
        v-model="title"
        placeholder="Title" 
        name="title" 
        id="title"
        required
        />
        <textarea v-model="description" id="description" placeholder=" Write something..." name="description" rows="6" required></textarea>
        <button type="submit" @click="onSubmit">Submit</button>
    </form>
</template>

<script>
import axios from 'axios';

export default {
    name: 'new_blog',
    data() {
        return {
            username: '',
            title: '',
            description: '',
        };
    },
    methods: {
        onSubmit(e) {
            this.$refs.formFields.reset();
            e.preventDefault();
            let params = {
                username: this.username,
                title: this.title,
                description: this.description
            }
            console.log(params)

            axios.post('https://blog-site-backend.wase-zahin.repl.co/create', params)
                .then((res) => {
                    console.log(params)
                    console.log(res.data);
                })
                .catch((err) => {
                    console.log(err);
                });
        },
    }
};
</script> 