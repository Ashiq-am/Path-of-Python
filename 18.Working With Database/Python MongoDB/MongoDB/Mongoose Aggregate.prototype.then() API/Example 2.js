// Require mongoose module
const mongoose = require("mongoose");

// Set Up the Database connection
mongoose.connect("mongodb://localhost:27017/geeksforgeeks", {
	useNewUrlParser: true,
	useUnifiedTopology: true,
});

const studentSchema = new mongoose.Schema({
	name: String,
	rollNumber: Number
});

const Student = mongoose.model('Student', studentSchema);

const agg = Student.aggregate([
	{ $project: { name: 1, rollNumber: 1 } }])

agg.then((successCB, errorCB) => {
	if (successCB) {
		console.log(successCB)
	}
	else {
		console.log(errorCB)
	}
})
