// Require mongoose module
const mongoose = require("mongoose");

// Set Up the Database connection
mongoose.connect("mongodb://localhost:27017/geeksforgeeks", {
	useNewUrlParser: true,
	useUnifiedTopology: true,
});

// Define the user schema
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
	},
	height: {
		type: Number,

		// Define the getter function
		get: (value) => {
			return value * 30.48
		}
	}
});

const User = mongoose.model('User', userSchema);

const user = new User({
	name: "User1", age: 25,
	weight: 68.5, height: 5.8
})
user.save()
console.log('Height in cm -', user.height)
