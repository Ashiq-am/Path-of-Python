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

const iplPlayerSchema = new mongoose.Schema({
	_id: Number,
	name: String,
	teamName: String,
	nationality: String
});

const Cricketer = mongoose.model('Cricketers', cricketerSchema);
const IplPlayer = mongoose.model('IplPlayers', iplPlayerSchema);

const aggregate = Cricketer.aggregate(
	[{ $project: { nationality: 1, _id: 0 } }]
)

aggregate.unionWith({
	coll: "iplplayers",
	pipeline: [{ $project: { _id: 0, nationality: 1 } }]
}).then(result => {
	console.log(result)
}).catch(err => {
	console.log(err)
})
