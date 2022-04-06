## 安装
```
npm install pxb-tools
```

## 导入

```js
const tools = require('pxb-tools')

```

## 格式化时间
```js
const dtstr = tools.dateFrame(new Date())
console.log(dtstr)
```

## 转义html中的特殊字符
```js
const htmlstr = tools.htmlEscape('<h1>我是xxx</h1>')
console.log(htmlstr)
```

## 还原html中的特殊字符
```js
const htmlunstr = tools.htmlunEscape(htmlstr)
console.log(htmlunstr)
```

## 开源协议
ISC
