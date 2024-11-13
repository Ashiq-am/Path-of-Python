//index.js

const mongoose = require('mongoose');

const setup = async () => {
	await mongoose.connect('mongodb://127.0.0.1:27017/GFG')
				.then(console.log('Connected to MongoDB')).catch(error =>
						console.error('Failed to connect to MongoDB:', error));


	// Define the schema
	const userSchema = new mongoose.Schema({
		email: { type: String, unique: true },
		name: String,
		age: Number,
	});

	// Create a model based on the schema
	const User = mongoose.model('User', userSchema);

	// Find a user and update their age
	const findUserAndUpdateAge = async () => {
		try {
			// Use await to get the result of findOneAndUpdate
			const user = await User.findOneAndUpdate({ email: 'example@example.com' },
													{ age: 30 },
													{ new: true }
													);
			console.log(user, "User Updated");
		} catch (err) {
			console.log(err);
		}
	};

	// Call the update function
	await findUserAndUpdateAge();

};

// Call the setup function to execute the code
setup();
