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
  guestbook: {
    url: '/guestbook',
    method: GET
  }


}
