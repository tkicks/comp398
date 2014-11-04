// Retrieve
var MongoClient = require('mongodb').MongoClient;

// Connect to the db
MongoClient.connect("mongodb://demoUser:passwd1@ds047440.mongolab.com:47440/tkicks", function(err, db) {
	if(err) { return console.dir(err); }

	console.dir("connected");

	var i,
		counter = 0;
	var collection = db.collection('hw14');
	var T = '01010100';
	var Y = '01011001';
	var L = '01001100';
	var E = '01000101';
	var R = '01010010';

	if (collection.find(function(err, result) {}) !== null) {
		collection.remove(function(err, result) {});
		console.dir("removed collection's documents");
	}

	db.createCollection('hw14', {strict:true}, function(err, collection) {});

	for (i = 0; i < 2500; i++)
	{
		if (counter === 0) {
			collection.insert({"letter":T}, {w:1}, function(err, result) {});
			counter++;
		}
		else if (counter === 1) {
			collection.insert({"letter":Y}, {w:1}, function(err, result) {});
			counter++;
		}
		else if (counter === 2) {
			collection.insert({"letter":L}, {w:1}, function(err, result) {});
			counter++;
		}
		else if (counter === 3) {
			collection.insert({"letter":E}, {w:1}, function(err, result) {});
			counter++;
		}
		else if (counter === 4) {
			collection.insert({"letter":R}, {w:1}, function(err, result) {});
			counter++;
		}
		if (counter === 5) {
			counter = 0;
		}
	}

	console.dir('added documents to hw14');

});