<template>
    <main>
        <h1><span>All Blogs</span></h1>
        <nav>
            <ul>
                <li v-for="blog in blogs_list" :key="blog.id">
                    <router-link class="blog_links" :to="{path:'/blog_description', query:{id:blog.id}}"><h3 class="blog_list">{{ blog.title }}</h3></router-link>
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
            axios.get('https://blog-site-backend.wase-zahin.repl.co/home')
                .then((res) => {
                    if (res) {
                        this.blogs_list = res.data
                        this.$forceUpdate();
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