import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/cadastro',
      name: 'cadastro',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/CadastroEscalaView.vue')
    },
    {
      path:'/list/policiais',
      name:'listarpolicial',
      component: () => import('../views/PolicialListView.vue')

    },
    
    {
      path: '/policiais/add',
      name: 'addpolicial',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/CadastroPolicialView.vue')
    },
    
    {
      path:'/policialdetail/:id',
      name:'/policialdetail',
      component: () => import('../views/PolicialDetailView.vue')

    }
  ]
})

export default router
