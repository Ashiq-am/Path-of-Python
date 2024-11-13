const mongoose = require('mongoose');

// Database connection
mongoose.connect('mongodb://127.0.0.1:27017/geeksforgeeks', {
	useNewUrlParser: true,
	useUnifiedTopology: true
});

// User model
const User = mongoose.model('User', {
	name: { type: String },
	age: { type: Number }
});

// Find only one document matching
// the condition(age >= 21)
User.findOne({ age: { $gte: 21 } }, function (err, res) {
	if (err) {
		console.log(err)
	}
	else {
		console.log("Result : ", res);
	}
});
