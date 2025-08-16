# Backend

## Docker Setup

### Building the Docker Image

```bash
docker build -t stashforlater-backend .
```

### Running the Container

```bash
docker run -p 8000:8000 stashforlater-backend
```

The application will be available at `http://localhost:8000`

### Environment Variables

The application expects the following environment variables (configure via `.env` file in the parent directory):

- `PROJECT_NAME` - Name of the project
- `POSTGRES_SERVER` - PostgreSQL server hostname
- `POSTGRES_PORT` - PostgreSQL port (default: 5432)
- `POSTGRES_USER` - PostgreSQL username
- `POSTGRES_PASSWORD` - PostgreSQL password
- `POSTGRES_DB` - PostgreSQL database name

### Development

For development with environment variables:

```bash
docker run -p 8000:8000 --env-file ../.env stashforlater-backend
```