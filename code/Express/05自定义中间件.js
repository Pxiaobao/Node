const express = require('express')
const qs = require('./06自定义中间件模块')
const app = express()
app.use(qs.ss)
app.post('/user',(req,res)=>{
    res.send(req.body)
})
app.listen(80,()=>{
    
})