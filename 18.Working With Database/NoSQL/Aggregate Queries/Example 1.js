// Requiring module
const mongoose = require("mongoose");

// Assumption is in our local, we have "UserDB"
// named mongoDB database available
mongoose.connect(
	"mongodb://localhost:27017/UserDB",
	function (err, db) {

		console.log("Connected correctly to server");

		// "UserValidation" named collection
		// available and each document contains
		// "salary" named column
		var col = db.collection('UserValidation');

		// By applying aggregate functionality,
		// finding the summation of salary and
		// the result is in "summedUpDocument"
		col.aggregate([{
			$group:
				{ _id: null, total: { $sum: '$salary' } }
		}]).toArray(function (err, summedUpDocument) {

			// Summed up salary value can be printed
			// as like below
			console.log(summedUpDocument[0].total)
			db.close();
		})
	});
