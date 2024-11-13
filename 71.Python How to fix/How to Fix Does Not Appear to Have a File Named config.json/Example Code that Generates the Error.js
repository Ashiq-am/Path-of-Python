const fs = require('fs');

try {
    const data = fs.readFileSync('config.json', 'utf8');
    const config = JSON.parse(data);
    console.log('Config:', config);
} catch (err) {
    console.error('Error reading config.json:', err.message);
    process.exit(1);
}
