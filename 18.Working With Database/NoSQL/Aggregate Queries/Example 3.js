// Requiring module
const mongoose = require("mongoose");

// Assumption is in our local, we have
// "UserDB" named mongoDB database
// available
mongoose.connect(
	"mongodb://localhost:27017/UserDB",
	function (err, db) {

	console.log("Connected correctly to server");

	// "UserValidation" named collection
	// available and each document contains
	// "salary" named column
	var col = db.collection('UserValidation');

	// By applying aggregate functionality,
	// finding the summation of salary
	// Here applied match condition where
	// matching address equal to Chennai
	// We are calculating total, average,
	// minimum and maximum amount
	col.aggregate([
		{ $match: { address: { $eq: "Chennai" } } },
		{
			$group:
			{
				_id: null, totalSalary: { $sum: "$salary" },
				averageSalary: { $avg: "$salary" },
				minimumSalary: { $min: "$salary" },
				maximumSalary: { $max: "$salary" }
			}
		}
	]).toArray(function (err, projectFunctionality) {
		console.log("Total Salary ..",
			projectFunctionality[0].totalSalary)

		console.log("Average Salary ..",
			projectFunctionality[0].averageSalary)

		console.log("Minimum Salary ..",
			projectFunctionality[0].minimumSalary)

		console.log("Maximum Salary ..",
			projectFunctionality[0].maximumSalary)
		db.close();
	})
});
