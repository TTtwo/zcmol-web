import md5 from 'js-md5'
import {GRAVATAR, DEFAULT_GRAVATAR, DEFAULT_GRAVATAR2} from "./constant";

export function getAvatar(email, style = true) {
  let default_gravatar = DEFAULT_GRAVATAR
  if (!email) email = '123'
  if (!style) default_gravatar = DEFAULT_GRAVATAR2
  // const src = GRAVATAR
  //   + md5(email)
  //   + '?&d='
  //   + default_gravatar
  //   + '&r=PG'
  const src = GRAVATAR + md5(email)
  return src
}

export function timeTransform(time) {
  const date = new Date(time * 1000)
  const yms = date.toLocaleDateString().replace(new RegExp('/', 'g'), '.')
  const hms = date.toLocaleTimeString()
  return yms + hms
}

