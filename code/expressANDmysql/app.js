const express = require('express')
const session = require('express-session')
const mysql = require('mysql')
const jwt = require('jsonwebtoken')
const expressjwt= require('express-jwt')
const app = express()
app.use(express.urlencoded({extended:false}))
app.use(session({
    secret:'pxb',
    resave:false,
    saveUninitialized:true
}))

const secrtkey = 'pxb_0306 ^_^'
app.use(expressjwt({secret:secrtkey,algorithms:['HS256']}).unless({path:['/login']}))

//denglu
app.post('/login',(req,res)=>{
    if(req.body.username !=='root' || req.body.password!=='root'){
        return res.send({
            status:0,
            message:'登陆失败'
        })
    }
    req.session.user = req.body
    req.session.islogin = true
    res.send({
        status:1,
        message:'登录成功',
        token:jwt.sign({username:req.body.username},secrtkey,{expiresIn:'500s'})
    })
})
//获取用户姓名的接口
app.get('/username',(res,req)=>{
    if(!req.session.islogin) return res.send({status:0,message:'fail'})
    res.send({
        status:1,
        message:'success',
        username:req.session.user.username
    })
})

//tuichu登录的接口
app.post('/logout',(req,res)=>{
    req.session.destory()
    res.send({
        status:1,
        msg:'tuichu 成功'
    })
})
app.listen(80,()=>{
    console.log('running at  port')
})