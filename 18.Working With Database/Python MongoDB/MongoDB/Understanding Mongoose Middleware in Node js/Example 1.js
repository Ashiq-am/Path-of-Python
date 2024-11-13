// express --> index.js
// connect to mongodb using mongoose.connect

const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/my_database')
  .then(() => console.log('Connected to MongoDB'))
  .catch(error => console.error('Connection error:', error));
