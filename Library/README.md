# Library

The **Library** project is a multi-module Spring Boot application demonstrating a microservices architecture with a service and client component.

## Modules

| Module | Description | Port |
|--------|-------------|------|
| [library-service](./library-service/) | Backend REST API and web application | 9080 |
| [library-client](./library-client/) | Frontend client consuming the service | 8080 |

## Architecture

```
┌─────────────────┐       REST API        ┌─────────────────┐
│  library-client │ ──────────────────►   │ library-service │
│   (Port 8080)   │   Basic Auth          │   (Port 9080)   │
└─────────────────┘                       └─────────────────┘
                                                   │
                                                   ▼
                                          ┌───────────────┐
                                          │  H2 Database  │
                                          └───────────────┘
```

## Technology Stack

- **Java**: 21
- **Spring Boot**: 3.5.7
- **Build Tool**: Maven
- **Database**: H2 (embedded)
- **UI**: Thymeleaf + Custom CSS
- **API Documentation**: Springdoc OpenAPI (Swagger UI)
- **Security**: Spring Security with Basic Auth for REST APIs

## Quick Start

### 1. Build Both Projects

```bash
# Build library-service
cd library-service
./buildMaven.sh

# Build library-client
cd ../library-client
./buildMaven.sh
```

### 2. Run the Services

```bash
# Terminal 1 - Start library-service
cd library-service
./runMaven.sh

# Terminal 2 - Start library-client
cd library-client
./runMaven.sh
```

### 3. Access the Applications

| Application | URL |
|-------------|-----|
| Library Service | http://localhost:9080/library-service/ |
| Library Client | http://localhost:8080/library-client/ |
| Swagger UI | http://localhost:9080/library-service/swagger-ui/index.html |
| H2 Console | http://localhost:9080/library-service/h2 |

## Default Credentials

- **Username**: `admin`
- **Password**: `Admin123`

## Author

- Rohtash Lakra

