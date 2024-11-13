const express = require('express');
const session = require('express-session');

const app = express();

// Set up session middleware
app.use(session({
	secret: 'mySecretKey', // used to sign the session ID cookie
	resave: false, // do not save the session if it's not modified
	// do not save new sessions that have not been modified
	saveUninitialized: false
}));

// Middleware to log session data
app.use((req, res, next) => {
	console.log('Session:', req.session);
	next();
});

// Route to set session data
app.get('/set-session', (req, res) => {
	req.session.user = { id: 1, username: 'GfG User' };
	res.send('Session data set');
});

// Route to get session data
app.get('/get-session', (req, res) => {
	if (req.session.user) {
		res.send('Session data: '
			+ JSON.stringify(req.session.user));
	} else {
		res.send('No session data found');
	}
});

// Route to destroy session
app.get('/destroy-session', (req, res) => {
	req.session.destroy((err) => {
		if (err) {
			console.error('Error destroying session:', err);
			res.send('Error destroying session');
		} else {
			res.send('Session destroyed');
		}
	});
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
	console.log(`Server is listening on port ${PORT}`);
});
