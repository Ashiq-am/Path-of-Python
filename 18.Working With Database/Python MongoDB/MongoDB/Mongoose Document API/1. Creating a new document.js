const mongoose = require("mongoose");

// Database connection
mongoose.connect("mongodb://127.0.0.1:27017/geeksforgeeks", {
	useNewUrlParser: true,
	useUnifiedTopology: true,
});

// User model
const User = mongoose.model("User", {
	name: { type: String },
	age: { type: Number },
});

// Creating a new dummy user document
const newUser = new User({
	name: "Ayush",
	age: 20,
});

// Save it to the database
newUser.save((err, res) => {
	if (err) return handleError(err);
	else return console.log("Result: ", res)
});

// For inserting multiple documents
User.insertMany(
	[
		{
			name: "Rishu",
			age: 21,
		},
		{
			name: "Megha",
			age: 24,
		},
		{
			name: "Aman",
			age: 16,
		},
		{
			name: "Riya",
			age: 18,
		},
	],
	(err, res) => {
		if (err) return handleError(err);
		else return console.log("Result: ", res)
	}
);
