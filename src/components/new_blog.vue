<template>
    <form class="newBlog" @submit="onSubmit">
        <input 
        v-model="title"
        type="text"
        placeholder="Title" 
        name="title" 
        id="title" />
        <textarea v-model="description" type="text" id="description" placeholder=" Write something..." name="description" rows="6"></textarea>
        <button type="submit" @click="onSubmit">Submit</button>
    </form>
</template>

<script>
import axios from 'axios';

export default {
    name: 'new_blog',
    data() {
        return {
            msg: 'Hello!',
            title: '',
            description: '',
        };
    },
    methods: {
        onSubmit(e) {
            e.preventDefault();
            let params = {
                title: this.title,
                description: this.description
            }
            console.log(params)
            axios.post('http://127.0.0.1:8000/home', params)
                .then(function (res) {
                    console.log(res.data);
                    
                    // if (res) {
                    //     return
                    // }
                    // else {
                    //     return
                    // }
                })
                .catch(function (err) {
                    console.log(err);
                });
        },
    }
};
</script> 