const express = require('express')

const app = express()

//定义一个最简单的中间健函数  可以理解为全局路由守卫
const mv = function(req,res,next){
    console.log('这是第一个中间件函数')
    //获取请求到达服务器的时间
    const time = new Date()
    req.startTime = time
    next()
}
//定义第二个中间健
const mv2 = function(req,res,next){
    console.log('这是第二个中间件函数')
    next()
}
//定义第三个中间件函数,注意这里没有使用app.use将其注册为全局生效，
//所以需要在定义路由的时候主动加上要使用的中间件
const mv3 = function(req,res,next){
    console.log('这是第三个中间件函数')
    //获取请求到达服务器的时间
    next()
}
//将mv注册为全局生效的中间件
app.use(mv)
app.use(mv2)

//定义一个路由
app.get('/',(req,res)=>{
    throw new Error('fuwuqi cuowu')
    res.send('main page'+req.startTime)
})

app.get('/user',(req,res)=>{
    res.send('user page')
})
//定义一个路由，使用第三个中间件
app.get('/manage',mv3,(req,res)=>{
    res.send('manage page')
})

//定义捕获错误的中间件；注意捕获错误的中间件有四个参数，且必须放到路由的最后
const errormv = function(err,req,res,next){
    console.log(err.message)
    res.send('error:'+err.message)
}
app.use(errormv)
app.listen(80,()=>{
    console.log('running')
})