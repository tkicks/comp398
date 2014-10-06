var addNode = (function(data) {
		this.stuff = data;
		this.next = null;
	}
	var stuff = null;
	var next = null;

console.log(addNode("things"));




















































// to "push"
var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World\n');
}).listen(1337, '127.0.0.1');
console.log('Server running at http://127.0.0.1:1337/');