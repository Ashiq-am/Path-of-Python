// server.js
const express = require('express');
const swaggerUi = require('swagger-ui-express');
const fs = require('fs');

const app = express();
const port = 3000;

// Read the OpenAPI specification
const openApiSpec = JSON.parse(fs.readFileSync('openapi.json', 'utf-8'));

// Serve the Swagger UI
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(openApiSpec));

app.listen(port, () => {
  console.log(`Swagger UI available at http://localhost:${port}/api-docs`);
});
