const { MongoClient } = require('mongodb');
const url = 'mongodb://localhost:27017';
const client = new MongoClient(url);
const database = 'e-comm';

async function getData() {
	let result = await client.connect();
	let db = result.db(database);
	let collection = db.collection('products');

	collection.aggregate([
		{ $group: { _id: "$price", relevance: { $sum: 1 } } },
		{ $sort: { relevance: -1 } }
	]).toArray(function (err, result) {
		if (err) throw err;
		console.log(result);
	});
}

getData();
