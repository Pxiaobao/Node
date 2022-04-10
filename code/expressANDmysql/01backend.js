const mysql = require('mysql')

const db = mysql.createPool({
    host:'127.0.0.1',
    port:'3306',
    user:'root',
    password:'root',
    database:'node_database'
})
//查询
db.query('select * from users',(err,results)=>{
    if(err) return console.log(err.message)
    console.log(results)
})
//插入
const user = {
    username:'pxb',
    age:'3'
}
const sqlStr = 'insert into users (username,age) values (?,?)'
db.query(sqlStr,[user.username, user.age],(err,results)=>{
    if(err) return console.log(err.message)
    if(results.affectedRows == 1) {
        console.log('插入成功')
    } 
})
//插入二
const sqlStr2 = 'insert into users set ?'
db.query(sqlStr2,user,(err,results)=>{
    if(err) return console.log(err.message)
    if(results.affectedRows == 1) {
        console.log('插入成功')
    } 
})
//更新
const sqlStr3 = 'update users set username=?,age=? where id=?'
db.query(sqlStr3,[user.username, user.age,user.id],(err,results)=>{
    if(err) return console.log(err.message)
    if(results.affectedRows == 1) {
        console.log('更新成功')
    } 
})
//更新2
const sqlStr4 = 'update users set ? where id=?'
db.query(sqlStr4,[user,user.id],(err,results)=>{
    if(err) return console.log(err.message)
    if(results.affectedRows == 1) {
        console.log('更新成功')
    } 
})
//删除
