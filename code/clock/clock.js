const fs = require('fs')
const path = require('path')

const stylereg = /<style>[\s\S]*<\/style>/
const scriptreg = /<script>[\s\S]*<\/script>/

let file = new Promise((resolve,reject)=>{
    fs.readFile(path.join(__dirname,'/index.html'),'utf8',(err,data)=>{
        if(err){
            reject(err)
        }else{
            resolve(data)
        }
    })
})

file.then((data)=>{
    let r1 = stylereg.exec(data)[0].replace('<style>','').replace('</style>','')
    fs.writeFile(path.join(__dirname,'style.css'),r1,()=>{})
    
    let r2 = scriptreg.exec(data)[0].replace('<script>','').replace('</script>','')
    fs.writeFile(path.join(__dirname,'script.js'),r2,()=>{})

    let r3 = data.replace(stylereg.exec(data)[0],'<link rel="stylesheet" href="./style.css" />').replace(scriptreg.exec(data)[0],'<script src="./script.js"></script>')
    fs.writeFile(path.join(__dirname,'Ht.html'),r3,()=>{})
}).catch((err)=>{
    console.log(err.message)
})