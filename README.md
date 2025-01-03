# Ngrok + Traefik + App

Demonstration on how to setup a docker compose project with Traefik and Ngrok.
The goal is to get a valid HTTPS connection to a locally running app.

## Usage

1. Create an account on <https://ngrok.com/>
2. Create an authtoken <https://dashboard.ngrok.com/get-started/your-authtoken>
3. Create a free ngrok domain <https://dashboard.ngrok.com/domains>

Copy `.env.example` to `.env` and replace the placeholders with your authtoken and ngrok domain.

Run `docker compose up` to start the project.

Access your services locally:

- App: <http://app.localhost>
- Traefik Dashboard: <http://traefik.localhost:8080>

Access your app via ngrok:

> [!NOTE]
> Replace `your.domain.ngrok-free.app` with your ngrok domain.

- Domain-based: <https://your.domain.ngrok-free.app>
- Path-based: <https://your.domain.ngrok-free.app/app>
