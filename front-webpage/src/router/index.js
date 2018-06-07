import Vue from 'vue'
import Router from 'vue-router'
import Index from '../components/Index'
import DailyArticle from '../components/DailyArticle'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/index',
      name: 'index',
      component: Index
    },
    {
      path: '/daily_article',
      name: 'daily_article',
      component: DailyArticle
    }
  ]
})
