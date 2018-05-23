var mongoose = require('mongoose');

// create a user model
var User = mongoose.model('User', {
  oauthID: Number,
  name: String,
  firstname: String,
  lastname: String,
  email: String,
  type: String,
  waytrn1: Array,
  age: String,
  profilepic: String,
  profilelink: String,
  gender: String,
  location:String,
  coord: Array,
  created: Date,
  education: String,
  major: String,
  screen_name: String,
  description: String,
  created_at: String,
  favourites_count: Number,
  statuses_count: Number
});


module.exports = User;
