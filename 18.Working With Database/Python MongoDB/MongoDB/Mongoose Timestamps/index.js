const mongoose = require("mongoose");

// Database connection
mongoose.connect("mongodb://localhost:27017/geeksforgeeks");

// Creating Schema
const studentSchema = new mongoose.Schema({
		name: { type: String, required: true },
		age: { type: Number, default: 8 },
	},
	{ timestamps: true }
);

// Student model
const Student = mongoose.model("Student", studentSchema);

// Creating Student document from Model

// Function to save in database
const saveStudent = async (name, age) => {
	let s = new Student({
		name: name,
		age: age,
	});
	s.save().then((doc) => {
		console.log("Name:", doc.name, ", Age:", doc.age);
		console.log("Created At:", doc.createdAt);
		console.log("Updated At:", doc.updatedAt);
	});
};

const updateStudent = async () => {
	let doc = await Student.findOneAndUpdate(
		{ name: "Rahul" },
		{ age: 25 },
		{ new: true }
	);
	console.log("Name:", doc.name, ", Age:", doc.age);
	console.log("Created At:", doc.createdAt);
	console.log("Updated At:", doc.updatedAt);
};

const start = async () => {
	await saveStudent("Rahul", 15);
	setTimeout(function () {
		updateStudent();
	}, 3000);
};

start();
