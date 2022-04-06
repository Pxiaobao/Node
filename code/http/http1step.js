//导入http模块
const http = require('http')
//创建web服务器实例
const server  = http.createServer();
//为实例绑定request事件
server.on('request',(req,res)=>{
    console.log('i am rquest')
})
//启动服务器
server.listen(80,()=>{
    console.log('server running on localhost')
})
