// Retrieve
var MongoClient = require('mongodb').MongoClient;

// Connect to the db
MongoClient.connect("mongodb://<uname>:<pwd>@ds047440.mongolab.com:47440/tkicks", function(err, db) {
	if(err) { return console.dir(err); }

	console.dir("connected");

	var collection = db.collection('test');
	var doc1 = {'pi':'3'};
	// db.collection('test', function(err, collection) {});
	// console.dir("Test collection not yet created. Add documents to create.");

	// db.collection('test', {strict:true}, function(err, collection) {});
	// console.dir("If collection !exist error");

	// db.createCollection('test', function(err, collection) {});
	// console.dir("Create a collection on Mongodb database");

	if(collection) {
		db.collection.remove();
	}

	db.createCollection('test', {strict:true}, function(err, collection) {});
	collection.insert(doc1, {w:1}, function(err, result) {});
	console.dir("inserted first digit of pi");
	// console.dir("This should be an error...");

});