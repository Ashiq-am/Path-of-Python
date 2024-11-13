// Server.js

app.get("/", function (req, res) {

	// Finding all the transactions
	Transaction.find({}, function (err, docs) {

		// We are not going to use res.send() function
		// res.send(docs);

		// Using res.render() method instead of
		// res.send() method
		// Using res.render() method, we can
		// pass data to the front-end
		res.render("index", {
			docs: docs,
		});
	});
});
