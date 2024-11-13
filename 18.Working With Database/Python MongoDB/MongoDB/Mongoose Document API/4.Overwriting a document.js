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

// OverWrite a document using `replaceOne()` method

User.replaceOne(
	{ name: "Rishu" },
	{ name: "Raja", age: 19 }, (err) => {
	if (err) return console.error(err);
	else {
		console.log('{ name: "Rishu" } is replaced
			with {name: "Raja", age: 19}')
	}
});
