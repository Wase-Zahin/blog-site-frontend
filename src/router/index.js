import login_page from "../components/login_page.vue";
import { createWebHistory, createRouter } from "vue-router";

const routes = [
  {
    path: "/login_page",
    name: "login_page",
    component: login_page,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;