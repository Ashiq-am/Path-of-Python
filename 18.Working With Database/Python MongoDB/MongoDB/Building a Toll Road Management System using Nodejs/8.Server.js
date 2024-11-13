// Server.js

const bodyParser = require("body-parser");

// Allowing our app to use bodyParser
app.use(
	bodyParser.urlencoded({
		extended: true,
	})
);
