const qs = require('querystringify')
function ss(req,res,next){
    //定义中间件具体的逻辑
    //1.定义一个str字符串，专门用来存储客户端发过来的请求体
    let str = ''
    //2.监听req的data事件
    req.on('data',(chunk)=>{
        str+=chunk
    })
    //3.监听req的end事件
    req.on('end',()=>{
        const body = qs.parse(str)
        req.body = body;
        next()
        console.log(body)
    })

}
function add(a,b){
    return a+b
}
module.exports = {
    ss
}