// dbUser.js
import mongoose from 'mongoose'

const userSchema = mongoose.Schema({
	email : String,
	displayName : {type : String, default : "User"},
	photoUrl :
		{type : String, default : "<DEFAULT_PROFILE_PICTURE_URL>"},
	speed : {type : Number, default : 1},
	strokeColor : {type : String, default : "red"},
	textColor : {type : String, default : "black"},
	guitar : {
		m_ratio1 : {type : Number, default : 0},
		n_ratio1 : {type : Number, default : 0},
		m_ratio2 : {type : Number, default : 0},
		n_ratio2 : {type : Number, default : 0},
		m_ratio3 : {type : Number, default : 0},
		n_ratio3 : {type : Number, default : 0},
		m_ratio4 : {type : Number, default : 0},
		n_ratio4 : {type : Number, default : 0},
	}
})

export default mongoose.model('userInfo', userSchema)
