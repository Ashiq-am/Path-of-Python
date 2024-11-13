// Require mongoose module
const mongoose = require("mongoose");

// Set Up the Database connection
const con = mongoose.createConnection("mongodb://localhost:27017/geeksforgeeks", {
useNewUrlParser: true,
useUnifiedTopology: true,
});

const userSchema = new mongoose.Schema({
name: String,
fixedDeposit: Number,
interest: Number,
tenure: {type:Number, default:6}
});

const User = con.model('User', userSchema);

console.log(con.modelNames());
