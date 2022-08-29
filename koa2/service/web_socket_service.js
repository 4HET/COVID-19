// const fso = require('fs')
const WebSocket = require('ws')
const path = require('path')
const fileUtils = require('../utils/file_utils')
const getDate = require('../utils/get_data')
const { fstat } = require('fs')
const { findSourceMap } = require('module')
const wss = new WebSocket.Server({
  port: 9998
})

module.exports.listen = () => {
  function sleep(d) {
    for (var t = Date.now(); Date.now() - t <= d;);
  }



  // wss.on('connection', client => {
  //   console.log('有客户端连接成功了~')
  //   client.on('message', async msg => {
  //     console.log(' 客户端发送数据给服务端了：' + msg)
  //     let payload = JSON.parse(msg)
  //     const action = payload.action
  //     if (action == 'getData') {
  //       let filePath = '../data/' + payload.chartClass + '/' + payload.chartClass + payload.chartDate + '.json'
  //       filePath = path.join(__dirname, filePath)
  //       console.log(filePath)
  //       // if(!fso.FileExists(filePath))
  //       // const f = false
  //       getDate.getFileJsonData(payload.chartClass)
        
  //       // if (f==true) 

  //       // for (var t = Date.now(); Date.now() - t <= 3000;);
  //       // console.log('file get')
  //       // const ret = await fileUtils.getFileJsonData(filePath)
        
  //       // console.log('file read :' + filePath)
        
  //       // payload.data = ret
  //       // console.log(JSON.stringify(payload))
  //       // for (var t = Date.now(); Date.now() - t <= 3000;);
        
  //       // client.send(JSON.stringify(payload))
  //       // client.send(JSON.stringify(ret))
  //       // client.send('hello socket from backend')

  //     }
  //     else {
  //       wss.clients.forEach(client => {
  //         client.send(msg)
  //       })
  //     }
      
      
  //   })
  // })
  wss.on('', client => {
    // console.log('有客户端连接成功了~')
    // client.on('message', async msg => {
      // console.log(' 客户端发送数据给服务端了：' + msg)
      // let payload = JSON.parse(msg)
      // const action = payload.action
      // if (action == 'getData') {
        // let filePath = '../data/' + payload.chartClass + '/' + payload.chartClass + payload.chartDate + '.json'
        // filePath = path.join(__dirname, filePath)
        // console.log(filePath)
        // if(!fso.FileExists(filePath))
        // const f = false
        getDate.getFileJsonData('add')
        
        // if (f==true) 

        // for (var t = Date.now(); Date.now() - t <= 3000;);
        // console.log('file get')
        // const ret = await fileUtils.getFileJsonData(filePath)
        
        // console.log('file read :' + filePath)
        
        // payload.data = ret
        // console.log(JSON.stringify(payload))
        // for (var t = Date.now(); Date.now() - t <= 3000;);
        
        // client.send(JSON.stringify(payload))
        // client.send(JSON.stringify(ret))
        // client.send('hello socket from backend')

      // }
      // else {
        // wss.clients.forEach(client => {
          // client.send(msg)
        // })
      // }
      
      
    // })
  })
}