// javascript program to solve
// the given question

// Create class for hotel data.
class Hotel {

	constructor(){
		this.name = "";
		this.roomAvl = 0;
		this.location = "";
		this.rating = 0;
		this.pricePr = 0;
	}
}

// Create class for user data.
class User{

	constructor(){
		this.uname = "";
		this.uId = 0;
		this.cost = 0;
	}
}

// Function to Sort Hotels by
// Bangalore location
function sortByBan(A, B)
{
	return B.name.localeCompare(A.name);
}

// Function to sort hotels
// by rating.
function sortByr(A, B)
{
	return A.rating > B.rating;
}

// Function to sort hotels
// by rooms availability.
function sortByRoomAvailable(A, B)
{
	return A.roomAvl < B.roomAvl;
}

// Print hotels data.
function PrintHotelData(hotels)
{
	console.log("PRINT HOTELS DATA:");
	console.log("HotelName"
		+ " "
		+ "Room Available"
		+ " "
		+ "Location"
		+ " "
		+ "Rating"
		+ " "
		+ "PricePer Room:");

	for (let i = 0; i < 3; i++) {
		console.log(hotels[i].name
			+ "		 "
			+ hotels[i].roomAvl
			+ "			 "
			+ hotels[i].location
			+ "	 "
			+ hotels[i].rating
			+ "		 "
			+ hotels[i].pricePr);
	}
	console.log();
}

// Sort Hotels data by name.
function SortHotelByName(hotels)
{
	console.log("SORT BY NAME:");

	hotels.sort(sortByBan);
	// console.log("h9");
	// console.log(hotels);
	for (let i = 0; i < hotels.length; i++) {
		console.log(hotels[i].name + " " + hotels[i].roomAvl + " "
			+ hotels[i].location + " "
			+ hotels[i].rating + " "
			+ " " + hotels[i].pricePr);
	}
	console.log();
}

// Sort Hotels by rating
function SortHotelByRating(hotels)
{
	console.log("SORT BY A RATING:");

	hotels.sort(sortByr);

	for (let i = 0; i < hotels.length; i++) {
		console.log(hotels[i].name + " "
			+ hotels[i].roomAvl + " "
			+ hotels[i].location + " "
			+ hotels[i].rating + " "
			+ " " + hotels[i].pricePr);
	}
	console.log();
}

// Print Hotels for any city Location.
function PrintHotelBycity(s, hotels)
{
	console.log("HOTELS FOR " + s + " LOCATION IS:");

	for (let i = 0; i < hotels.length; i++) {

		if (hotels[i].location == s) {

			console.log(hotels[i].name + " "
				+ hotels[i].roomAvl + " "
				+ hotels[i].location + " "
				+ hotels[i].rating + " "
				+ " " + hotels[i].pricePr);
		}
	}
	console.log();
}

// Sort hotels by room Available.
function SortByRoomAvailable(hotels)
{
	console.log("SORT BY ROOM AVAILABLE:");

	hotels.sort(sortByRoomAvailable);
	for (let i = hotels.length - 1; i >= 0; i--) {

		console.log(hotels[i].name + " " + hotels[i].roomAvl + " " + hotels[i].location + " " + hotels[i].rating + " " +hotels[i].pricePr);
	}
	console.log();
}

// Print the user's data
function PrintUserData(userName,
				userId,
				bookingCost, hotels)
{

	let user = [];


	// Access user data.
	for (let i = 0; i < 3; i++) {
		let u = new User();
		u.uname = userName[i];
		u.uId = userId[i];
		u.cost = bookingCost[i];
		user.push(u);
	}

	// Print User data.
	console.log("PRINT USER BOOKING DATA:")
	console.log("UserName UserID HotelName BookingCost")

	for (let i = 0; i < user.length; i++) {
		console.log(user[i].uname + "		 " + user[i].uId + "	 " + hotels[i].name + "		 " + user[i].cost);
	}
}

// Functiont to solve
// Hotel Management problem
function HotelManagement(userName,userId, hotelName,
bookingCost, rooms, locations, ratings, prices)
{
	// Initialize arrays that stores
	// hotel data and user data
	let hotels = [];

	// Create Objects for
	// hotel and user.


	// Initialise the data
	for (let i = 0; i < 3; i++) {
		let h = new Hotel();
		h.name = hotelName[i];
		h.roomAvl = rooms[i];
		h.location = locations[i];
		h.rating = ratings[i];
		h.pricePr = prices[i];
		hotels.push(h);
	}
	console.log();

	// Call the various operations
	PrintHotelData(hotels);
	SortHotelByName(hotels);
	SortHotelByRating(hotels);
	PrintHotelBycity("Bangalore", hotels);
	SortByRoomAvailable(hotels);
	PrintUserData(userName, userId, bookingCost, hotels);
}

// Driver Code.
// Initialize variables to stores
// hotels data and user data.
let userName = ["U1", "U2", "U3"];
let userId = [2, 3, 4];
let hotelName = ["H1", "H2", "H3" ];
let bookingCost = [1000, 1200, 1100 ];
let rooms = [4, 5, 6 ];
let locations = ["Bangalore", "Bangalore", "Mumbai" ];
let ratings = [5, 5, 3 ];
let prices = [100, 200, 100 ];

// Function to perform operations
HotelManagement(userName, userId, hotelName, bookingCost,
rooms, locations, ratings, prices);

// the code is contributed by Nidhi goel.
