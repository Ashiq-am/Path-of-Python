// Server.js continued

// Transaction schema is the schema for our
// records that we are going to store
// It contains vehicleNumber in the form of
// string, date as string, time as string
// and the toll amount as number
const transactionSchema = new mongoose.Schema({
	vehicleNumber: String,
	date: String,
	time: String,
	tollAmount: Number,
});
