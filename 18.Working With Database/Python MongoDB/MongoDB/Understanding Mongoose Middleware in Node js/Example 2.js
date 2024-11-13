// index.js

const userSchema = new mongoose.Schema({
  username: String,
  email: String,
  age: Number
});

const User = mongoose.model('User', userSchema);
