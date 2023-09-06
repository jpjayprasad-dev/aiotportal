# AIOT Portal

This is a Django application helps managing Data and Control of Aiot Devies.

### Steps:
 - Clone this git repo.

    `git clone https://github.com/jpjayprasad-dev/aiotportal/`

 - Build a docker image using the Dockerfile in root directory of this repo.

    `docker build -t <image_name> .`

 - start the container.

    `docker container run --rm -p 8800:8800
    -e POSTGRES_HOST=<postgres_host> \
    -e POSTGRES_PORT=<postgres_port> \
    -e POSTGRES_DB=$MG_DB \
    -e POSTGRES_USER=<postgres_user> \
    -e POSTGRES_PASSWORD=<postgres_password> \
    --name aiot-portal <image_name>`

 - go to browser localhost:8800
