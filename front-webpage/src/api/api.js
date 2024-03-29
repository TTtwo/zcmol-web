const
  GET = 'get',
  POST = 'post',
  DELETE = 'delete',
  HEAD = 'head',
  PUT = 'put',
  PATCH = 'patch'

export default {
  BASEURL: 'http://162.14.81.168:8889/api',

  index: {
    url: '/index',
    method: GET
  },
  motto: {
    url: '/motto',
    method: GET
  },
  get_guestbook: {
    url: '/guestbook',
    method: GET
  },
  post_guestbook: {
    url: '/guestbook',
    method: POST
  },
  get_daily: {
    url: '/:id/daily',
    method: GET
  },
  get_daily_comment: {
    url: '/:id/comments',
    method: GET
  },
  post_daily_comment: {
    url: '/:id/comments',
    method: POST
  }
}
