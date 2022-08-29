module.exports.getFileJsonData = async(name) => {
    const fs = require('fs');
    const child_process = require('child_process');
    
    var workerProcess =  child_process.exec('python '+'./utils/api/api/'+name+'.py', function (error) {
        if (error) {
            console.log(error.stack);
            console.log('Error code: ' + error.code);
            console.log('Signal received: ' + error.signal);
        }
        console.log('successful running news.py');
        
    });

    workerProcess.on('exit', function (code) {
        console.log('子进程已退出，退出码 ' + code);
        
    });
     
}