// Require mongoose module
const mongoose = require("mongoose");

// Set Up the Database connection
mongoose.connect("mongodb://localhost:27017/geeksforgeeks", {
	useNewUrlParser: true,
	useUnifiedTopology: true,
});

const userSchema = new mongoose.Schema({
	name: String,
	bornYear: Number
});

const User = mongoose.model('User', userSchema);

User.aggregate([{ $project: { _id: 0, bornYear: 1 } }])
	.exec((error, result) => {
		if (error) {
			console.log(error);
		} else {
			console.log(result);
		}
	})
