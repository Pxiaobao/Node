function dateFrame(dtStr){
    const dt = new Date(dtStr)
    const year = dt.getFullYear()
    const month = padZero(dt.getMonth()+1)
    const day = padZero(dt.getDate())
    const hh = padZero(dt.getHours())
    const mm = padZero(dt.getMinutes())
    const ss = padZero(dt.getSeconds())
    return `${year}-${month}-${day} ${hh}:${mm}:${ss}`

}

function padZero(num){
    return num>9?num:'0'+num
}
module.exports ={
    dateFrame
}