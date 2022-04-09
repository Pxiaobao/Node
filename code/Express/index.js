import axios from 'axios'
const get = document.querySelector('#get')
const p = document.querySelector('#p')
get.addEventListener('click',()=>{
    axios({
        url:'http://127.0.0.1/api/get',
        method:'GET',
        data:{
            name:'zs',
            age:'25'
        }
    }).then((res)=>{
        p.innerHTML = res
    })
})