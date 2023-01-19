import login_page from "../components/login_page.vue";
import home_page from "../components/home_page.vue"
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
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;