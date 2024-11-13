// convertSchema.js
const { readFileSync, writeFileSync } = require('fs');
const { graphqlToOpenApi } = require('graphql-to-swagger');

// Read the GraphQL schema
const schema = readFileSync('schema.graphql', 'utf-8');

// Convert the GraphQL schema to OpenAPI
const openApiSpec = graphqlToOpenApi(schema);

// Write the OpenAPI specification to a file
writeFileSync('openapi.json', JSON.stringify(openApiSpec, null, 2));
