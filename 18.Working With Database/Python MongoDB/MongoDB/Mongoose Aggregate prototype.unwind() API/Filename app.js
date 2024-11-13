// Require mongoose module
const mongoose = require("mongoose");

// Set Up the Database connection
mongoose.connect("mongodb://localhost:27017/geeksforgeeks", {
	useNewUrlParser: true,
	useUnifiedTopology: true,
});

const statesSchema = new mongoose.Schema({
	stateId: Number,
	stateName: String,
	city: []
});

const State = mongoose.model('State', statesSchema);

const aggregate = State.aggregate();

aggregate.unwind("$city").then(result => {
	console.log(result)
}).catch(err => {
	console.log(err)
})
