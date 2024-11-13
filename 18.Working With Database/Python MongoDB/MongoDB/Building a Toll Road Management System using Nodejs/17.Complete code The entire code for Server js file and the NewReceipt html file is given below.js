// Server.js

const express = require("express");
const app = express();
const mongoose = require("mongoose");
const ejs = require("ejs");
app.set("view engine", "ejs");

const bodyParser = require("body-parser");

app.use(
	bodyParser.urlencoded({
		extended: true,
	})
);
app.set("view engine", "ejs");

mongoose.connect(
"mongodb://127.0.0.1/transactionDatabase", {
	useNewUrlParser: true,
	useUnifiedTopology: true,
});

const transactionSchema = new mongoose.Schema({
	vehicleNumber: String,
	date: String,
	time: String,
	tollAmount: Number,
});

const Transaction = mongoose.model(
	"Transaction", transactionSchema);

app.get("/", function (req, res) {
	Transaction.find({}, function (err, docs) {
		// res.send(docs);
		res.render("index", {
			docs: docs,
		});
	});
});

app.get("/newReceipt", function (req, res) {
	res.sendFile(__dirname + "/newReceipt.html");
});

app.post("/newReceipt", function (req, res) {
	var t = new Transaction({
		vehicleNumber: req.body.vehicleNumber,
		date: getDate(),
		time: getTime(),
		tollAmount: req.body.amount,
	});
	t.save();
	res.send("saved");
});

function getDate() {
	var date = new Date();
	date = date.toString();
	console.log(date.substring(0, 10));
	return date.substring(0, 10);
}

function getTime() {
	var today = new Date();
	return today.getHours() + ":"
		+ today.getMinutes() + ":"
		+ today.getSeconds();
}

app.listen(8080, function () {
	console.log("Server listening on port 8080");
});
