import Router from 'vue-router'
import Login from './components/Login'
import Index from './components/Index'
import Guestbook from './components/Guestbook'

const router = new Router({
  routes: [
    {path: '/login', name: 'login', component: Login},
    {
      path: '/index', name: 'index', component: Index, redirect: Guestbook, children: [
        { path: '/guestbook', name: 'guestbook', component: Guestbook}
      ]
    },
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

