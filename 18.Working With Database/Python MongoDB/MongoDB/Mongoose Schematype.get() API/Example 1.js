// Require mongoose module
const mongoose = require("mongoose");

// Set Up the Database connection
mongoose.connect("mongodb://localhost:27017/geeksforgeeks", {
	useNewUrlParser: true,
	useUnifiedTopology: true,
});

// Define a user schema
const userSchema = new mongoose.Schema({
	name: {
		type: String
	},
	age: {
		type: Number
	},
	weight: {
		type: Number,
		get: (value) => {
			return Math.ceil(value)
		}
	}
});

const User = mongoose.model('User', userSchema);

// Find the user by given ID
User.findById('63845defc7553ff921623ff9').then(result => {
	console.log(result.weight);
});
