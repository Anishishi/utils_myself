var http = require('http');
var net = require('net');

var hosttclc = '192.168.10.222';
var porttcpc = 50000;

function loopSleep(_loopLimit,_interval, _mainFunc){
  var loopLimit = _loopLimit;
  var interval = _interval;
  var mainFunc = _mainFunc;
  var i = 0;
  var loopFunc = function () {
    var result = mainFunc(i);
    if (result === false) {
      // break機能
      return;
    }
    i = i + 1;
    if (i < loopLimit) {
      setTimeout(loopFunc, interval);
    }
  }
  loopFunc();
}

var client = net.createConnection(porttcpc, hosttclc);

function doSomething(){
  //var client = net.createConnection(porttcpc, hosttclc);
  console.log('st send');
  if(client.write('hogehoge')){console.log('send done.')};
}

client.on( 'data', function( data ){
  console.log( 'send back : ' + data );
})

// client.on('end', function(){
//   console.log('end');
// });
// client.on('close', function(){
//   console.log('close');
// });

loopSleep(3, 15000, function(i){
  doSomething();
});

function myend(){console.log('fin');}


//var client = new net.Socket();
setTimeout(myend, 100000);

// client.connect(porttcpc, hosttclc, function(){
//   console.log('接続');
//   client.write('hogehoge');
//   client.end();
//   console.log('safely done.');
// });

//setTimeout(printend, 1000);
