//database.js

import mysql from 'mysql2'

// Create a MySQL connection pool
const pool = mysql.createPool({
	host: 'localhost', //MYSQL_HOST you can also use 127.0.0.1
	user: 'root', //MYSQL_USER
	password: 'YOUR_MYSQL_PASSWORD',
	database: 'notes_app'//DEFINE YOUR DATABASE NAME,
}).promise()

// Function to get all notes from database
export async function getNotes() {
	//Query to select all notes available in your Database notes table
	const [rows] = await pool.query("SELECT * FROM notes")
	return rows;
}
