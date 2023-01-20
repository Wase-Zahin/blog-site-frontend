<template>
    <main>
        <h1><span>{{ title }} </span></h1>
        <p>{{ description }}</p>
    </main>
</template>

<script>
import axios from 'axios';
import router from '@/router';
import { useRoute, useRouter } from 'vue-router';

// import { useRoute, useRouter } from 'vue-router';
export default {
    data() {
        return {
            title: '',
            description: '',
            route: useRoute(),
            router: useRouter(),
        }
    },
    methods() {
        
    },
    mounted() {
        console.log(this.route.query.id);
        if(window.localStorage.getItem('login_status') == 'login_yes') {
            let params = {
                id: this.route.query.id
            }
            axios.post('http://127.0.0.1:8000/description', params)
            .then((res) => {
                console.log(res.data);
                this.description = res.data.description
                this.title = res.data.title
            })
            .catch(function(err) {
                console.log(err);
            })
        }
        else {
            router.push({
                name: 'login_page'
            })
        }
    }
}
</script>