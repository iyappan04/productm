import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'products',
    component: () => import('../views/Products.vue')
  },
  {
    path: '/product/:id',
    name: 'product',
    props: true,
    component: () => import('../views/Product.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
