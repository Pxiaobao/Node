const express = require('express')

const router = express.Router()

router.get('/get',(req,res)=>{
    const query = req.query
    res.send({
        status:0,
        msg:'GET成功',
        data:query
    })
})
router.post('/post',(req,res)=>{
    //通过req.body获取请求体重包含的url-encoded的数据
    const query = req.body
    res.send({
        status:0,
        msg:'POST成功',
        data:query
    })
})
module.exports = router