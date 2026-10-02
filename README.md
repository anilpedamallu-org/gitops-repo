# First Deployment App

Tiny Python web app for testing deployments.

## Run on Windows or Mac

```bash
python app.py
```

Open:
http://localhost:8000

The page displays `1st deployment` in 20px Comic Sans MS.
The refresh counter is shown in the top-right corner.

Each browser refresh increments the counter exactly once.
Favicon requests and other paths are not counted.

## Docker

```bash
docker build -t first-deployment-app .
docker run --rm -p 8000:8000 first-deployment-app
```
