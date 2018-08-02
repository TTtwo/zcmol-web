import Vue from 'vue'
import Router from 'vue-router'
import Index from '../components/Index'
import DailyArticle from '../components/DailyArticle'
import Motto from '../components/Motto'
import Http from 'vue-resource'
import request_api from '../api/requet_api'
import VueParticles from 'vue-particles'
import iView from 'iview'

Vue.use(Router)
Vue.use(request_api)
Vue.use(Http)
Vue.use(iView)
Vue.use(VueParticles)

export default new Router({
  routes: [
    {
      path: '*',
      name: '404',
      redirect: '/index'
    },
    {
      path: '/index',
      name: 'index',
      component: Index
    },
    {
      path: '/:id/daily_article',
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
