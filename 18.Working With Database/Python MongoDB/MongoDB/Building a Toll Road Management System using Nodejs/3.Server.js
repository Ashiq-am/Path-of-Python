// Server.js continued

// Line below will connect our app to the local
// database with the name "transactionDatabase"
// which will store all of our toll transactions
mongoose.connect("mongodb://127.0.0.1/transactionDatabase", {
	useNewUrlParser: true,
	useUnifiedTopology: true,
});
