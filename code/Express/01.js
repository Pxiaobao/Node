//导入express
const express = require('express')
//创建web服务器
const app = express()
app.use(express.static('./public'))
app.get('/user',(req,res)=>{
    //调用res.send()方法，向客户端相应
    //req.query可以获取到请求所携带的参数，默认是一个空对象{}
    res.send(req.query)
})
app.get('/user/:id',(req,res)=>{
    //调用res.send()方法，向客户端相应
    //请求地址示例 http://127.0.0.1/user/78
    //req.params可以访问到请求中的：后面的动态参数，默认是一个空对象{}
    //req.params {"id":"78"}
    let a = req.params;
    res.send(a)
    
})
app.post('/user',(req,res)=>{
    //调用res.send()方法，向客户端相应
    res.send('post请求成功')
})

app.listen(80,()=>{
    console.log('runing')
})