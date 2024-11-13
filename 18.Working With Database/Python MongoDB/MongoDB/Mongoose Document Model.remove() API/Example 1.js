// Require mongoose module
const mongoose = require('mongoose');

// Set Up the Database connection
mongoose.connect(
	'mongodb://localhost:27017/geeksforgeeks', {
	useNewUrlParser: true,
	useUnifiedTopology: true
})

// Defining customerSchema schema
const customerSchema = new mongoose.Schema(
	{ name: String, orderCount: Number, superUser: Boolean}
)

// Defining customerSchema model
const Customer = mongoose.model('Customer', customerSchema);

Customer.remove().then(result => {
	console.log(result)
})
