import api from './api'
const apiConvert = function (url, args) {
  let res = url
  Object.keys(args).map(key => {
    res.replace(new RegExp(`:${key}`, 'g'), encodeURIComponent(args[key]))
  })
  return res
}

const base_url = api.BASEURL

export default {
  install: Vue => {
    Vue.prototype.$$api = async function (api = null, {urlArgs = null, body = null, params = null}) {
      if (api === null || typeof api !== "object")
        throw 'api is null or not a object'

      let url = base_url + api.url
      let meth = api.method
      let res

      if (urlArgs !== null)
        url = apiConvert(url, urlArgs)

      if (['get', 'delete', 'head'].includes(meth)) {
        res = await this.$http[meth](url, {params})
      }
      else {
        res = await this.$http[meth](url, body)
      }

      return res
    }
  }
}
