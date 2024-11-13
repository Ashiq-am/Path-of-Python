// Server.js

// Handling the home route
app.get("/", function (req, res) {

	// Fetching all the transaction data from
	// the database
	Transaction.find({}, function (err, docs) {

		// Sending the transactions found as
		// a response to this route
		res.send(docs);
	});
});
