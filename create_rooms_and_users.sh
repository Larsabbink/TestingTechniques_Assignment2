#!/bin/bash

until curl -s "http://localhost:8008/_synapse/admin/v1/ping" > /dev/null; do
    sleep 1
done

# Create users
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"username": "user1", "password": "password", "auth": {"type":"m.login.dummy"}}' \
     "http://localhost:8008/_matrix/client/r0/register"

# Create rooms
# curl -X POST  \
#      -H "Content-Type: application/json" \
#      -d '{"preset": "public_chat", "name": "Room1"}' \
#      "http://localhost:8008/_synapse/admin/v1/createRoom"


# Add users to rooms, etc.

# Keep the container running
# tail -f /dev/null