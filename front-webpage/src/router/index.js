import Vue from 'vue'
import Router from 'vue-router'
import Index from '../components/Index'
import DailyArticle from '../components/DailyArticle'
import Motto from '../components/Motto'
import Http from 'vue-resource'
import request_api from '../api/requet_api'
import iView from 'iview'

Vue.use(Router)
Vue.use(request_api)
Vue.use(Http)
Vue.use(iView)

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
    },
    {
      path: '/motto',
      name: '/motto',
      component: Motto
    }
  ]
})
