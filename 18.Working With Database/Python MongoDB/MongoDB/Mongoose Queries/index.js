const mongoose = require("mongoose");

// Database connection
mongoose.connect("mongodb://localhost:27017/geeksforgeeks",);

// Creating Schema
const studentSchema = new mongoose.Schema({
	name: { type: String, required: true },
	age: { type: Number, default: 8 },
	highschool: { type: Boolean, default: false },
});

// Student model
const Student = mongoose.model("Student", studentSchema);
// Creating Student document from Model

// function to save in database
const saveStudent = async (name, age) => {
	let s = new Student({
		name: name,
		age: age,
	});
	await s.save();
	console.log("student document saved in database\n " +
        "Student name:", s.name);
};

const updateHighSchool = async () => {
	await Student.updateMany(
		{ age: { $gt: 12 } },
		{ highschool: true });
	console.log("Updated student fields");
};

const start = async () => {
	await saveStudent("Ajay", 5);
	await saveStudent("Rajesh", 13);
	await saveStudent("Manav", 15);
	updateHighSchool();
};

start();
