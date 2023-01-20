import login_page from "../components/login_page.vue";
import home_page from "../components/home_page.vue";
// import blog_section from "../components/blog_section.vue";
import blog_description from "../components/blog_description.vue";
import { createWebHistory, createRouter } from "vue-router";

const routes = [
  {
    path: "/login",
    name: "login_page",
    component: login_page,
  },
  {
    path: "/home",
    name: "home_page",
    component: home_page,
  },
  {
    path: "/blog_description",
    name: "blog_description",
    component: blog_description,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;