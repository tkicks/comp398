/*
	linkedList creates an empty linked list to host the nodes
	@param = none
	@return = none
*/
var linkedList = function() {
	this.head = null;
}

/*
	makeNode creates a node with null next and lastNodes
	it will also set the cargo to the value passed in data
	@param = <string> data
	@return = none
*/
var makeNode = function(data) {
	this.stuff = data;
	this.nextNode = null;
	this.last = null;
	}

/*
	addNode adds the node to the linked list
	if there is no init node in the list, 
	the node passed in will become the first
	otherwise the list will be traversed to the end
	and it will be added there
	@param = <Element> node
	@return = none
*/
var addNode = function(node) {
	var currentNode = linkedList.head,
	firstNode;

	/*
		if there is not a current node (empty list)
		make this node the first
	*/
	if (!currentNode) {
		linkedList.head = node;
		firstNode = linkedList.head;
	}

	else {

		/*
			while there are still nodes in the list
			keep moving to the next
		*/
		while (currentNode.nextNode)
		{
			currentNode = currentNode.nextNode;
		}

		/*
			add the passed in node to next value of
			the last node and set the last value of
			the passed in node to the last node 
		*/
		currentNode.nextNode = node;
		node.last = currentNode;
	}
}

/*
	printList will print out the cargo of each node
	in the linked list
	@params = none
	@return = none
*/
var printList = function() {
	var currentNode = linkedList.head,
	counter = 0;

	/*
		while the current node exists log an index counter
		and the cargo to the console
		goes past last one to log it to console as well
	*/
	while (currentNode) {
		console.log(counter + '. ' + currentNode.stuff);
		currentNode = currentNode.nextNode;
		counter++;
	}
}

/*
	printListReverse will traverse to the end of the list
	and then print the cargo of each node back to the
	beginning of the list
	@params = none
	@return = none
*/
var printListReverse = function() {
	var currentNode = linkedList.head;

	// stops at last node with a value
	while (currentNode.nextNode) {
		currentNode = currentNode.nextNode;
	}

	// goes past last one to log it to console as well
	while (currentNode !== null) {
		console.log(currentNode.stuff);
		currentNode = currentNode.last;
	}
}

/*
	findVal will search the linked list for the passed
	in value and log its index to the console
	@params = <string> val
	@return = none
*/
var findVal = function(val) {
	var location = 0,
	currentNode = linkedList.head,
	found = false;

	// while there's still a node with a value
	while (currentNode) {

		// if the current node's cargo equals value log
		if (currentNode.stuff === val) {
			console.log('Found ' + val + ' at location: ' + location);
			found = true;
			break;
		}

		// otherwise advance the node and index counter
		else {
			currentNode = currentNode.nextNode;
			location++;
		}
	}

	// if the value isn't in the linked list log its absence
	if (!found) {
		console.log('Value not found');
	}
}


linkedList();

// hard coded ===================================
var node = new makeNode('Moran');
addNode(node);
node = new makeNode('Thad');
addNode(node);
node = new makeNode('Mascot');
addNode(node);
node = new makeNode('Donnie');
addNode(node);
node = new makeNode('Harmon');
addNode(node);
node = new makeNode('Larry');
addNode(node);
node = new makeNode('Mary Jo');
addNode(node);
node = new makeNode('Kate');
addNode(node);
node = new makeNode('Kara');
addNode(node);
node = new makeNode('Billy');
addNode(node);
node = new makeNode('Radon');
addNode(node);
node = new makeNode('Debra');
addNode(node);
node = new makeNode('Shilo');
addNode(node);
node = new makeNode('Dean');
addNode(node);
node = new makeNode('Cougar');
addNode(node);
node = new makeNode('Coach');
addNode(node);
node = new makeNode('Jon Jon');
addNode(node);
node = new makeNode('Gilday');
addNode(node);
node = new makeNode('Denise');
addNode(node);
// ==============================================


// file io ======================================
// var node, data;
// var fs = require('fs');
// // fs.open('test.txt', 'r', 0666);
// // fs.open('output.txt', 'w', 0666);
// fs.read('test.txt', data, )
// ==============================================


printList();
// printListReverse();
findVal('Shilo');
