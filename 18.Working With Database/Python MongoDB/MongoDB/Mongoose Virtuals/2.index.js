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

// Setting the firstname and lastname using set method
userSchema.virtual('name.full')
	.get(function () {
		return this.name.first + ' ' + this.name.last;
	})
	.set(function (value) {
		var fname = value.split(' ');
		this.name.first = fname[0];
		this.name.last = fname[1];
	})

// Creating mongoose model
const User = mongoose.model('user', userSchema);

const newUser = new User({
	name: {
		full: "Dave Bautista"
	}
})

newUser.save()
	.then(u => {
		console.log("FIRSTNAME: ", u.name.first,
					"\nLASTNAME:", u.name.last)
	})
	.catch(error => {
		console.log(error);
	})
