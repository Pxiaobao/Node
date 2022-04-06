//导入http模块
const http = require('http')
//创建web服务器实例
const server  = http.createServer();
//为实例绑定request事件
server.on('request',(req,res)=>{
    //req是请求对象，包括请求的相关数据与属性
    //req.url
    //req.method
    let str = `您请求的方法是 ${req.url},method is ${req.method}`
    console.log(str)
    //调用res.setHeader方法设置中文编码格式
    //调用res.end方法，像服务端响应
    res.setHeader('Content-Type','text/html; charset=utf-8')
    res.end(str)
})
//启动服务器
server.listen(80,()=>{
    console.log('server running on localhost')
})