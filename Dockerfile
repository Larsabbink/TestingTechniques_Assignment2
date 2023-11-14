FROM matrixdotorg/synapse:latest

# RUN mkdir /data
# RUN mkdir /data/logs
# RUN chmod -R 777 /data

COPY homeserver.yaml /data/homeserver.yaml