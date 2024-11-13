// Requiring module
const mongoose = require('mongoose');
const express = require('express');
const app = express();

// Connecting to database
mongoose.connect('mongodb://localhost:27017/GFG',
	{
		useNewUrlParser: true,
		useUnifiedTopology: true,
		useFindAndModify: false
	});

// Constructing mongoose schema
const userSchema = new mongoose.Schema({
	name: {
		first: String,
		last: String
	}
});

// Setting virtual property using get method
userSchema.virtual('name.full')
	.get(function () {
		return this.name.first + ' ' + this.name.last;
	})

// Creating mongoose model
const User = mongoose.model('user', userSchema);

const newUser = new User({
	name: {
		first: "David",
		last: "Beckham"
	}
})

newUser.save()
	.then(u => {
		console.log("USERNAME: ", u.name.full)
	})
	.catch(error => {
		console.log(error);
	})
