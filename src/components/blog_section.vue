<template>
    <main>
        <h1><span>All Blogs</span></h1>
        <nav>
            <ul>
                <li v-for="blog in blogs_list" :key="blog.id">
                    <router-link :to="{path:'/blog_description', query:{id:blog.id}}"><h3>{{ blog.title }}</h3></router-link>
                    <p v-if="blog.description.length<50">{{ blog.description }} </p>
                    <p v-else>{{ blog.description.substring(0,50)+"..." }}</p>
                </li>
            </ul>
        </nav>
    </main>
</template>

<script>
import axios from 'axios';

export default {
    name: 'blog_section',
    data() {
        return {
            blogs_list: [],
        };
    },
    mounted() {
        this.onMount();
    },
    methods: {
        onMount() {
            axios.post('http://127.0.0.1:8000/home')
                .then((res) => {
                    if (res) {
                        this.blogs_list = res.data
                    }
                    else return
                })
                .catch(function (err) {
                    console.log(err);
                });
        },
        
    }
};
</script> 