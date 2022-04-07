const express = require('express')
//创建路由模块
const router = express.Router();

router.get('/user/list',(req,res)=>{
    res.send('get reequest ')
})

router.post('/user/add',(req,res)=>{
    res.send('post reequest ')
})

module.exports = router