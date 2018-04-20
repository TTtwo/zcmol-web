import Router from 'vue-router'
import Login from './components/Login'
import Index from './components/Index'

const router = new Router({
  routes:[
    { path: '/login', name: 'login', component: Login},
    { path: '/index', name: 'index', component: Index}
  ]
})

// router.beforeEach((to, from, next) =>{
//   const token = localStorage.getItem('token')
//   if (!token && to.name !== 'login') {
//     next('/login')
//   } else {
//     next()
//   }
// })

export default router

