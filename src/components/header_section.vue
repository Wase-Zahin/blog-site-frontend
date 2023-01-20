<template>
    <header>
        <div class="headerTop">
            <h1 @click="backToHome">BLOG SITE</h1>
            <button class="openPopUp">Logout</button>
        </div>
        <div class="navWrapper">
            <h2>Content</h2>
            <nav>
                <ul>
                    <li></li>
                    <li></li>
                </ul>
            </nav>
        </div>
        <hr />
    </header>
</template>

<script>
import router from '@/router';

export default {
    methods: {
        backToHome() {
            setTimeout(() => {
                    router.push({
                    name: 'home_page'
                })    
            }, 500);
        },
    }
}
</script>