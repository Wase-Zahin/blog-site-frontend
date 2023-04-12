<template>
   <div class="logins">
    <form ref="loginFields" class="login-box" @submit="onSubmit">
        <img class="login-icon" src="../components/img/6681204.png"/>
        <h1>User Login</h1>
        <input 
        v-model="username"
        placeholder="Username" 
        name="username" 
        id="username" required/>

        <input
        v-model="password" 
        type="password"
        id="password" 
        placeholder="Password" 
        name="password" required/>
        <button type="submit">Login</button>
    </form>
   </div>
</template>

<script>
import router from '@/router';
import axios from 'axios';

export default {
    name: 'login_page',
    data() {
        return {
            msg: 'Hello!',
            username: '',
            password: '',
        };
    },
    methods: {
        onSubmit(e) {
            e.preventDefault();
            let params = {
                username: this.username,
                password: this.password
            }
            axios.post('https://blog-site-backend.wase-zahin.repl.co/login', params)
            .then(function (res) {
                if (res.data.status == 'login_no') alert('Login Credentials Incorrect')
                if (res.data.status == 'login_yes') {
                    let userId = res.data.id;
                    window.localStorage.setItem('login_status', res.data.status);
                    window.localStorage.setItem('username', params.username);
                    window.localStorage.setItem('userid', userId)
                    setTimeout(() => {
                            router.push({
                            name: 'home_page'
                        })    
                    }, 1500);
                } else return
            })
            .catch(function (err) {
                console.log(err);
            });
        },
    }
};
</script> 