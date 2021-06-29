import Tasks from '../components/Tasks.vue'
import Task from '../components/Task.vue'
import {createRouter, createWebHashHistory} from 'vue-router';

const routes = [
  {path: '/', component: Tasks},
  {path: '/task', component: Task},
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;

