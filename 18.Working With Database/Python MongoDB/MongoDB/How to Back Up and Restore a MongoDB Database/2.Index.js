const Express = require("express");
const connectDB = require("./connect");
const app = Express();

const PORT = 8000;

// Basic route for testing
app.get("/", (req, res) => {
	res.send("welcome to the server.");
});

const start = async () => {
	try {
		await connectDB("mongodb://localhost:27017/DEMO_DB");
		app.listen(PORT, () => {
			console.log(`Server is running on port ${PORT}.`);
		});
	} catch (error) {
		console.log(error);
		console.log("Failed to connect to the database,server is not running.");
	}
};

start();
