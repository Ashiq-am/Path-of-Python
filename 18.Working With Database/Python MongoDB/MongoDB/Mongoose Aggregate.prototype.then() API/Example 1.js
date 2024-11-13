// Require mongoose module
const mongoose = require("mongoose");

// Set Up the Database connection
mongoose.connect("mongodb://localhost:27017/geeksforgeeks", {
	useNewUrlParser: true,
	useUnifiedTopology: true,
});

const userSchema = new mongoose.Schema({
	_id: Number,
	name: String,
	age: Number
});

const User = mongoose.model('User', userSchema);

User.aggregate([{ $project: { _id: 1, name: 1, age: 1 } }])
	.then((successCB, errorCB) => {
		if (successCB)
			console.log(successCB)
		else
			console.log(errorCB)
	})
