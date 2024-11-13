// Server.js continued

// Handling get request on our home route.
app.get("/newReceipt", function (req, res) {
	res.send("got request on newReceipt route");
});

// Allowing our app to listen on port 8080
app.listen(8080, function () {
	console.log("Server listening on port 8080");
});
