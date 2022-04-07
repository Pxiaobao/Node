const express = require('express')
const app = express()
//挂载路由模块
const router = require('./03route')
//注册路由模块
//app.use的作用就是注册全局中间件
app.use(router)
app.listen(80,()=>{
    console.log('http runing')
})

