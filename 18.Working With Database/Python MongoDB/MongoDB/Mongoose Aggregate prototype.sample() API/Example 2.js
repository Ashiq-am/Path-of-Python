// Require mongoose module
const mongoose = require("mongoose");

// Set Up the Database connection
mongoose.connect("mongodb://localhost:27017/geeksforgeeks", {
	useNewUrlParser: true,
	useUnifiedTopology: true,
});

const cricketerSchema = new mongoose.Schema({
	_id: Number,
	name: String,
	nationality: String
});

const Cricketer = mongoose.model('Cricketers', cricketerSchema);

Cricketer.aggregate([{ $sample: { "size": 4 } }])
	.exec((error, result) => {
		if (error) {
			console.log(error);
		} else {
			console.log(result);
		}
	})
