export const app_name = "早茶月光-管理"
export const editor_status = {
  insert: 0,
  update: 1
}
export const editor_type = {
  log: 0,
  blog: 1,
  motto: 2,
  saySomething: 3
}
export const editor_text = {
  [editor_type.log]: {type: editor_type.log, text: '日志'},
  [editor_type.blog]: {type: editor_type.blog, text: '博客'},
  [editor_type.motto]: {type: editor_type.motto, text: '鸡汤'},
  [editor_type.saySomething]: {type: editor_type.saySomething, text: '说说'}
}
export const menus = [
  {
    id: 1,
    text: '评论管理',
    sub_menus: [
      {
        id: 'guestbook',
        text: '留言',
        url: '/guestbook'
      },
      {
        id: 'articleComment',
        text: '日志评论',
        url: '/articleComment'
      },
      {
        id: 'blogComment',
        text: '文章评论',
        url: '/blogComment'
      }
    ]
  },
  {
    id: 2,
    text: '编辑内容',
    sub_menus: [
      {
        id: 'write',
        text: '编写发布',
        url: '/write'
      }
    ]
  },
  {
    id: 3,
    text: '内容管理',
    sub_menus: [
      {
        id: 'contentManager',
        text: '查看/修改',
        url: '/contentManager'
      }
    ]
  },
  {
    id: 4,
    text: '配    置',
    sub_menus: [
      {
        id: 'setting',
        text: '修改配置',
        url: '/setting'
      }
    ]
  }
]
export const MODALKEYTEXT = {
  id: 'id',
  nickName: '昵称',
  time: '时间',
  content: '内容',
  email: '邮箱',
  website: '网址',

  target_nickName: '回复对象',
  target_content: '回复对象的内容',

  reply_content: '回复内容',
  my_reply: '我的回复',

}
