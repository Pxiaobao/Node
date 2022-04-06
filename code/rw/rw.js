const fs  = require('fs')
const path = require('path')
const pathStr1 = path.join(__dirname,'test.txt')
const pathStr2 = path.join(__dirname,'output.txt')
let a = new Promise((resolve,reject)=>{
    fs.readFile(pathStr1,'utf8',(err,data)=>{
        if(err){
            reject(err.message)
        }else{
            const arr = data.split(' ')
            const newArr = []
            arr.forEach((ele)=>{
                newArr.push(ele.replace('=',':'))
            })
            let s = newArr.join('\r\n')
            resolve(s)

        }
    })
})
a.then((s)=>{
    fs.writeFile(pathStr2,s,(err)=>{
        if(err){console.log('err')}
    })
}).catch((e)=>{
    console.log(e)
})