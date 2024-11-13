// Server.js

// Adding require statement for express
const express = require("express");

// Making app variable using express
const app = express();

// Adding require statement for mongoose package
const mongoose = require("mongoose");

// Adding require statement for ejs
const ejs = require("ejs");

// Setting view engine to ejs
app.set("view engine", "ejs");

// Adding require statement for body-parser
const bodyParser = require("body-parser");
