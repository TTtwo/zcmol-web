import Router from 'vue-router'
import Login from './components/Login'
import Index from './components/Index'
import Guestbook from './components/Guestbook'
import ArticleComment from './components/ArticleComment'
import Write from './components/Write'
import ContentManager from './components/ContentManager'

const router = new Router({
  routes: [
    {path: '/login', name: 'login', component: Login},
    {
      path: '/index', name: 'index', component: Index, redirect: ContentManager, children: [
        { path: '/guestbook', name: 'guestbook', component: Guestbook},
        { path: '/articleComment', name: 'articleComment', component: ArticleComment},
        { path: '/write', name: 'write', component: Write},
        { path: '/contentManager', name: 'contentManager', component: ContentManager},
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

