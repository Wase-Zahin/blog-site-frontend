<template>
    <div class="headerofpage">
        <header>
            <div class="headerTop">
                <h1>BLOG SITE</h1>
                <button @click="showPopup = !showPopup" class="openPopUp">Logout</button>
            </div>
            <div class="navWrapper">
                <h2>Content</h2>
                <nav>
                    <ul>
                        <li v-for="tab in tabs" :key="tab" :class="['tab-button', { active: currentTab === tab }]"
                            @click="currentTab = tab"> {{ tab }}
                        </li>
                    </ul>
                </nav>
            </div>
            <hr />
        </header>
        <KeepAlive>
            <component :is="currentTab" class="tab"></component>
        </KeepAlive>
        <!-- popup style design -->
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
    </div>
</template>

<script>
import login_page from "./login_page.vue"
import new_blog from "./new_blog.vue";
import blog_section from "./blog_section.vue";
import router from '@/router';

export default {
    name: 'home_page',
    components: {
        login_page,
        new_blog,
        blog_section,
    },
    data() {
        return {
            blogs_list: [],
            currentTab: 'blog_section',
            tabs: ['blog_section', 'new_blog'],
            showPopup: false,
        }
    },
    methods: {
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