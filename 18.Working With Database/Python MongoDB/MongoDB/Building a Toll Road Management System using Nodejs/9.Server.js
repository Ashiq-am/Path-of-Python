// Server.js

// Handling post request on the /newReceipt route
app.post("/newReceipt", function (req, res) {

	// Getting the vehicle Number from the request,
	// which was entered in the newReceipt.html
	// page
	let vNo = req.body.vehicleNumber;

	// Getting the amount from the request.
	let amt = req.body.amount;

	// Creating a new transaction which we
	// are going to save in database.
	var t = new Transaction({
		vehicleNumber: vNo,
		date: getDate(),
		time: getTime(),
		tollAmount: amt,
	});

	// Saving the transaction in the database.
	t.save();

	// Sending response that we have saved the data
	res.send("Saved the data");
});

// Function to get the current date
function getDate() {

	// Creating new date object
	var date = new Date();

	// Converting date to string
	date = date.toString();

	// Returning the date
	return date.substring(0, 10);
}

// Function to get the current time
function getTime() {
	var today = new Date();
	return today.getHours() + ":"
		+ today.getMinutes()
		+ ":" + today.getSeconds();
}
