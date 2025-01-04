# Ngrok + Traefik + App

Demonstration on how to setup a docker compose project with Traefik and Ngrok.
The goal is to get a valid HTTPS connection to a locally running app.

## Usage

1. Create an account on <https://ngrok.com/>
2. Create an authtoken <https://dashboard.ngrok.com/get-started/your-authtoken>
3. Create a free ngrok domain <https://dashboard.ngrok.com/domains>

Copy `.env.example` to `.env` and replace the placeholders with your authtoken and ngrok domain.

Run `docker compose up` to start the project.
Access logs for the HTTP calls will be visible in the console.

Access your services locally:

- App: <http://app.localhost>
- Traefik Dashboard: <http://traefik.localhost> or <https://traefik.localhost>

Access your app via ngrok:

> [!NOTE]
> Replace `your.domain.ngrok-free.app` with your ngrok domain.

- Domain-based: <https://your.domain.ngrok-free.app>
- Path-based: <https://your.domain.ngrok-free.app/app>

## Good to know

> [!WARNING]
> On Windows/Mac use `host.docker.internal` instead of `host.docker.internal:host-gateway`

- ngrok needs access to the host to be able to push routes to the traefik router (this is accomplished with `extra_hosts: - "host.docker.internal:host-gateway"`)
- ngrok can rewrite the host header of the request to match an existing traefik route with `--request-header-add "host: my.route"` (this replaces the existing host header instead of adding another one)
