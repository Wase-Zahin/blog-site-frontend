<template>
    <form @submit="onSubmit">
        <input placeholder="username" name="username" id="username" />
        <input type="password" id="password" placeholder="Password" name="password" />
    </form>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
    name: 'new_blog',
    data() {
        return {
            msg: 'Hello!',
            username: ref(),
            password: ref(),
        };
    },
    methods: {
        onSubmit(values) {
            let params = {
                username: values.username,
                password: values.password
            }
            axios.post('http://127.0.0.1:5000/login', params)
            .then(function (res) {
                console.log(res);
            })
            .catch(function (err) {
                console.log(err);
            });
        },
    }
};
</script> 