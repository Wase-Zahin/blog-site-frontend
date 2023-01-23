<template>
    <header>
        <div class="headerTop">
            <h1 @click="backToHome">BLOG SITE</h1>
            <button @click="showPopup = !showPopup" class="openPopUp">Logout</button>
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
        <section v-if="showPopup" class="popupsection ShowPopUp">
            <div class="insidepopup">
                <p>Are you sure<br /> you want to logout?</p>
                <hr />
                <div class="button-design">
                    <button @click="logout">Confirm</button>
                    <hr />
                    <button @click="showPopup = false">Cancel</button>
                </div>
            </div>
        </section>
    </header>
</template>

<script>
import router from '@/router';

export default {
    data() {
        return {
            showPopup: false,
        }
    },
    methods: {
        backToHome() {
            setTimeout(() => {
                    router.push({
                    name: 'home_page'
                })    
            }, 500);
        },
        logout() {
            setTimeout(() => {
                router.push({
                    name: 'login_page'
                })
            }, 1000);
        },
    }
}
</script>