// Require mongoose module
const mongoose = require("mongoose");

// Set Up the Database connection
mongoose.connect("mongodb://localhost:27017/geeksforgeeks", {
	useNewUrlParser: true,
	useUnifiedTopology: true,
});

const studentSchema = new mongoose.Schema({
	studentId: Number,
	studentName: String,
	marks: []
});

const Student = mongoose.model('Student', studentSchema);

const aggregate = Student.aggregate();
aggregate.unwind("$marks").exec((err, result) => {
	if (err) {
		console.log(err)
	} else {
		console.log(result)
	}
})
