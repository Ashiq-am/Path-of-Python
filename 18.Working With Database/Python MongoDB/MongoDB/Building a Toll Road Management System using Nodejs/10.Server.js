// Server.js

// Handling request on home route
app.get("/", function (req, res) {
	res.send("got a request on home route");
});
