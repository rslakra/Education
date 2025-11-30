# Library Client

The **library-client** is a frontend web application that consumes the [library-service](../library-service/) REST API.

> For overall project documentation, see the [Library README](../README.md).

## Service URLs

| Resource | URL |
|----------|-----|
| Home | http://localhost:8080/library-client/ |
| Users | http://localhost:8080/library-client/users/list |

## Build & Run

```bash
# Build
./buildMaven.sh

# Run
./runMaven.sh
```

## Configuration

Key properties in `application.properties`:

| Property | Value | Description |
|----------|-------|-------------|
| `server.port` | 8080 | Server port |
| `server.servlet.contextPath` | /library-client | Context path |
| `apiHostBaseUrl` | http://localhost:9080/library-service/v1 | Library Service API URL |
| `libraryService.username` | admin | API authentication username |
| `libraryService.password` | Admin123 | API authentication password |

## Architecture

The client:
- **Disables local security** - No login required on the client
- **Uses Basic Auth** - Authenticates with library-service for REST calls
- **Calls REST API** - Fetches data from `/v1/users`, `/v1/roles`, etc.

## Prerequisites

The [library-service](../library-service/) must be running before starting the client.

## Features

- View and manage users via REST API
- Modern, responsive UI matching library-service design
- Secure communication using HTTP Basic Authentication

## Author

- Rohtash Lakra
