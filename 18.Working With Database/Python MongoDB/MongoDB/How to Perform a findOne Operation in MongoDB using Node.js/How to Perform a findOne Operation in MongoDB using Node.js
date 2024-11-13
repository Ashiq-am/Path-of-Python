//index.js

const { MongoClient } = require('mongodb');

async function main() {
    const uri = 'YOUR_URI';
    const client = new MongoClient(uri,
        {
            useNewUrlParser: true,
            useUnifiedTopology: true
        });

    try {
        await client.connect();
        console.log('Connected to database');

        const database = client.db('gfg');
        const collection = database.collection('students');

        // Insert sample data
        await collection.insertMany([
            { name: "Alice", age: 25, city: "Los Angeles" },
            { name: "Bob", age: 30, city: "San Francisco" },
            { name: "Charlie", age: 35, city: "Seattle" }
        ]);

        // Perform findOne operation
        const query = { name: "Alice" };
        const result = await collection.findOne(query);
        console.log('Found document:', result);

    } catch (error) {
        console.error('Error connecting to the database or performing the operation:', error);
    } finally {
        await client.close();
    }
}

main();
