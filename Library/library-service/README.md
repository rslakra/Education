# Library Service

The **library-service** is the backend REST API and web application for the Library system.

> For overall project documentation, see the [Library README](../README.md).

## Service URLs

| Resource | URL |
|----------|-----|
| Home | http://localhost:9080/library-service/ |
| Swagger UI | http://localhost:9080/library-service/swagger-ui/index.html |
| API Docs | http://localhost:9080/library-service/v3/api-docs |
| H2 Console | http://localhost:9080/library-service/h2 |
| Login | http://localhost:9080/library-service/login |

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
| `server.port` | 9080 | Server port |
| `server.servlet.contextPath` | /library-service | Context path |
| `spring.security.user.name` | admin | Default username |
| `spring.security.user.password` | Admin123 | Default password |

## Security

- **Web UI**: Form-based login at `/login`
- **REST API** (`/v1/**`): HTTP Basic Authentication
- **H2 Console**: Publicly accessible (CSRF disabled)
- **Swagger UI**: Publicly accessible

## Database Tables

```sql
SELECT * FROM addresses;
SELECT * FROM audit_logs;
SELECT * FROM files;
SELECT * FROM file_history;
SELECT * FROM roles;
SELECT * FROM sessions;
SELECT * FROM users;
SELECT * FROM users_roles;
SELECT * FROM user_security;
```

## REST API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/v1/users` | User management |
| `/v1/roles` | Role management |
| `/v1/files` | File management |
| `/v1/books` | Book management |

## Author

- Rohtash Lakra
