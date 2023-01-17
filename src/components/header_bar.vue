<template>
    <header>
        <div class="headerTop">
            <h1>BLOG SITE</h1>
            <!-- <login_page></login_page> -->
        </div>
        <div class="navWrapper">
            <h2>Content</h2>
            <nav>
                <ul>
                    <li
                        v-for="tab in tabs"
                        :key="tab"
                        :class="['tab-button', {active: currentTab === tab}]"
                        @click="currentTab = tab"
                    > {{ tab }}
                    </li>
                </ul>
            </nav>
        </div>
        <hr />
        <KeepAlive>
            <component :is="currentTab" class="tab"></component> 
        </KeepAlive>
    </header>
</template>

<script>
import login_page from "./login_page.vue"
import new_blog from "./new_blog.vue";
import blog_section from "./blog_section.vue";

export default {
    name: 'App',
    components: {
        login_page,
        new_blog,
        blog_section
    },
    data() {
        return {
            currentTab: 'blog_section',
            tabs: ['blog_section', 'new_blog']
        }
    }
}
</script>