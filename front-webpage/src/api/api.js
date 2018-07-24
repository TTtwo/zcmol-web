const
  GET = 'get',
  POST = 'post',
  DELETE = 'delete',
  HEAD = 'head',
  PUT = 'put',
  PATCH = 'patch'

export default {
  BASEURL: 'http://localhost:5000/api',

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
  }
}
