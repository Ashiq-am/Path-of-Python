// Server.js

// Handling the new receipt route
// passing the newReceipt.html file on this route
app.get("/newReceipt", function (req, res) {
	res.sendFile(__dirname + "/newReceipt.html");
});
