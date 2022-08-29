// 服务器的入口文件
// 1.创建KOA的实例对象
const Koa = require('koa')
const app = new Koa()
const getDate = require('./utils/get_data')
// 2.绑定中间件
// 绑定第一层中间件
var ls = ['add', 'input', 'map', 'news', 'sh_map', 'trend', 'wordCloud','policy']
function hello() {
    for (var t in ls)
        getDate.getFileJsonData(ls[t])
}

hello()
var t1 = setInterval(hello, 2*60*60*1000);

// var t2 = setInterval("hello()", 3000);

//去掉定时器的方法

// window.clearInterval(t1);
const respDurationMiddleware = require('./middleware/koa_response_duration')
app.use(respDurationMiddleware)
// 绑定第二层中间件
const respHeaderMiddleware = require('./middleware/koa_response_header')
app.use(respHeaderMiddleware)
// 绑定第三层中间件
const respDataMiddleware = require('./middleware/koa_response_data')
app.use(respDataMiddleware)
// 3.绑定端口号 8888
app.listen(8888)
const WebSocketService = require('./service/web_socket_service')
WebSocketService.listen()