<template>
    <header_section></header_section>
    <main class="blog_details">
        <h1><span>{{ title }} </span></h1>
        <h6>Written by {{ username }}</h6>
        <p>{{ description }}</p>
    </main>
</template>

<script>
import axios from 'axios';
import router from '@/router';
import { useRoute, useRouter } from 'vue-router';
import header_section from './header_section.vue';

// import { useRoute, useRouter } from 'vue-router';
export default {
    components: {
        header_section,
    },
    data() {
        return {
            username: '',
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
            axios.post('https://full-stack.wase-zahin.repl.co/description', params)
            .then((res) => {
                console.log(res.data)
                this.description = res.data.description
                this.title = res.data.title
                this.username = res.data.username
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