// Require mongoose module
const mongoose = require("mongoose");

// Set Up the Database connection
const URI = "mongodb://localhost:27017/geeksforgeeks"

const connectionObject = mongoose.createConnection(URI, {
useNewUrlParser: true,
useUnifiedTopology: true,
});

const Customer = connectionObject.model('Customer', new mongoose.Schema({
name: String,
address: String,
orderNumber: Number,
}));

const Student = connectionObject.model('Student', new mongoose.Schema({
name: String,
age: Number,
rollNumber: Number
}));

const modelDetails = connectionObject.modelNames();
console.log(modelDetails);
console.log(modelDetails.length);
