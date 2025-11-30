# Education

The **Education** repository contains educational projects demonstrating various software development concepts and technologies.

## Projects

| Project | Description | Technology |
|---------|-------------|------------|
| [Library](./Library/) | Multi-module library management system | Spring Boot 3.5.7, Java 21 |
| eLearning | Online training modules and courses | - |

## Folder Structure

```
/
├── Library/                    # Library Management System
│   ├── library-service/        # Backend REST API & Web App (Port 9080)
│   ├── library-client/         # Frontend Client (Port 8080)
│   └── README.md              # Library project documentation
├── eLearning/                  # Online training modules
├── README.md                   # This file
└── robots.txt                  # Search engine crawler configuration
```

## Quick Start

### Library Project

```bash
# 1. Build and run library-service
cd Library/library-service
./buildMaven.sh
./runMaven.sh

# 2. Build and run library-client (in a new terminal)
cd Library/library-client
./buildMaven.sh
./runMaven.sh
```

**Access:**
- Library Service: http://localhost:9080/library-service/
- Library Client: http://localhost:8080/library-client/

For detailed documentation, see the [Library README](./Library/README.md).

## Technology Stack

- **Java**: 21
- **Spring Boot**: 3.5.7
- **Build Tool**: Maven
- **Database**: H2 (embedded)
- **UI**: Thymeleaf
- **API Documentation**: Springdoc OpenAPI

## Author

- Rohtash Lakra
