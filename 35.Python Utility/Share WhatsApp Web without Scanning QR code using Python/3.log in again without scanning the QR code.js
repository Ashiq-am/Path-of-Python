function getResultFromRequest(request) {
	return new Promise((resolve, reject) => {
		request.onsuccess = function(event) {
			resolve(request.result);
		};
	})
}

async function getDB() {
	var request = window.indexedDB.open("wawc");
	return await getResultFromRequest(request);
}

async function injectSession(SESSION_STRING) {
	var session = JSON.parse(SESSION_STRING);
	var db = await getDB();
	var objectStore = db.transaction("user", "readwrite").objectStore("user");
	for(var keyValue of session) {
		var request = objectStore.put(keyValue);
		await getResultFromRequest(request);
	}
}

var SESSION_STRING = "";
await injectSession(SESSION_STRING);
