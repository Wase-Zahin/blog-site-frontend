import blog_section from "../components/blog_section.vue";
import { createWebHistory, createRouter } from "vue-router";

const routes = [
  {
    path: "/blog_section",
    name: "blog_section",
    component: blog_section,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;