// Requiring module
const MongoClient = require("mongodb");

// Connection URL
const url='mongodb://localhost:27017/';

// Our database name
const databasename="GFG";

MongoClient.connect(url).then((client) => {

	const connect = client.db(databasename);

	// Connecting to collection
	const collection = connect.collection("gfg2");

	// Function call with $or operator
	collection.find({$or:[{"name":"GFG"},{"marks":"10"}]}).toArray().then((ans)=>{
		console.log(ans);
	});

}).catch((err) => {
// Printing the error message
console.log(err.Message);
})
