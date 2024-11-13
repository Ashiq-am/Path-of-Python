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
		// matching address equal to
		// Chennai and result will be in
		// summedUpDocumentForChennai
		col.aggregate([
			{ $match: { address: { $eq: "Chennai" } } },
			{
				$group:
					{ _id: null, total: { $sum: '$salary' } }
			}
		]).toArray(function (err, summedUpDocumentForChennai) {

			// Summed up salary value can be printed
			// as like below
			console.log(summedUpDocumentForChennai[0].total)
			db.close();
		})
	});
