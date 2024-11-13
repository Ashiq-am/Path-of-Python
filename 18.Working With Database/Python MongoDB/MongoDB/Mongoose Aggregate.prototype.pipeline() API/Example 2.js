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

const currentPipeline = User
	.aggregate()
	.project({ name: 1 })
	.sortByCount({ 'bornYear': 1 })
	.pipeline()
console.log(currentPipeline)
