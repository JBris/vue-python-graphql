import Vue from 'vue'
import VueRouter from 'vue-router'
import SignUp from '@/components/SignUp.vue'

Vue.use(VueRouter)

  const routes = [
    {
        path: '/signup',
        name: 'SignUp',
        component: SignUp
    },
]

const router = new VueRouter({
  routes
})

export default router
