// Require mongoose module
const mongoose = require('mongoose');

// Set Up the Database connection
mongoose.connect(
	'mongodb://localhost:27017/geeksforgeeks', {
	useNewUrlParser: true,
	useUnifiedTopology: true
})

const userSchema = new mongoose.Schema(
	{ name: String }
)

// Defining userSchema model
const User = mongoose.model('User', userSchema);

User.remove().then(result => {
	console.log(result)
})

User.find({_id: '630db5818577bafc2709d603'}).
then(result => {
	console.log(result)
})
