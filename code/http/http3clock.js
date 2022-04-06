const http = require('http')
const fs = require('fs')
const path = require('path')
const server = http.createServer()
server.on('request',(req,res)=>{
    let url = req.url;
    let fpath = path.join(__dirname,'../clock',url)
    fs.readFile(fpath,'utf8',(err,data)=>{
        if(err){
            return res.end(fpath)
        }
        res.end(data)
    })
})
server.listen(80,()=>{
    console.log('reunning')
})