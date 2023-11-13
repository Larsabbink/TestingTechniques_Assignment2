FROM matrixdotorg/synapse:latest

COPY homeserver.yaml /data/homeserver.yaml

COPY create_rooms_and_users.sh /scripts/create_rooms_and_users.sh
RUN chmod +x /scripts/create_rooms_and_users.sh

# CMD ["/data/create_rooms_and_users.sh"]s