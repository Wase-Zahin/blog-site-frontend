<template>
    <form class="newBlog" @submit="onSubmit">
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
        onSubmit() {
            let params = {
                username: this.username,
                title: this.title,
                description: this.description
            }
            axios.post('http://127.0.0.1:8000/create', params)
                .then(function (res) {
                    console.log(params)
                    console.log(res.data);
                    if (res.data == "Submitted successfully") {
                        console.log('NICE')
                    }
                })
                .catch(function (err) {
                    console.log(err);
                });
        },
    }
};
</script> 