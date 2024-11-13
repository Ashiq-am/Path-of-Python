// Require mongoose module
const mongoose = require("mongoose");

// Set Up the Database connection
mongoose.connect("mongodb://localhost:27017/geeksforgeeks", {
	useNewUrlParser: true,
	useUnifiedTopology: true,
});

const phoneSchema = new mongoose.Schema({
	name: String,
	companyName: String,
	manufacturingYear: Number,
});

const Phone = mongoose.model('Phone', phoneSchema);

Phone.aggregate()
	.sortByCount('manufacturingYear')
	.then(result => {
		console.log(result);
	}).catch(err => {
		console.log(err);
	})
