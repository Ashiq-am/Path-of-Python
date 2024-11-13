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

// Update only one document matching
User.updateOne({ name: "Rishu" },
{ age: 22 }, function (err, res) {
	if (err) {
		console.log(err)
	}
});

// Or you can use findOneAndUpdate()

const doc = User.findOneAndUpdate(
	{ name: "Rishu" },
	{ age: 22 },

	// if 'new' isn't true then findOneAndUpdate()
	// will return the document as it was
	// before it was updated.

	{ new: true },
	function (err, res) {
		if (err) {
			console.log(err)
		}
		else {
			console.log("Result : ", res);
		}
	});
