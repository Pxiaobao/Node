const express = require('express')

const app = express()
//peizhi 解析body中的数据中间件
app.use(express.urlencoded({extended:false}))

//在路由之前配置cors这个中间件
// const cors = require('cors')
// app.use(cors)
const router = require('./08接口模块')
app.use('/api',router)


app.listen(80,()=>{
    console.log('running at 80 port')
})