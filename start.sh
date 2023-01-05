# . ./auth.sh
# docker run -p 5000:5000 \
#     -e APP_SECRET_KEY=$APP_SECRET_KEY \
#     -e AUTH0_CLIENT_ID=$AUTH0_CLIENT_ID \
#     -e AUTH0_CLIENT_SECRET=$AUTH0_CLIENT_SECRET \
#     -e AUTH0_DOMAIN=$AUTH0_DOMAIN \
#     -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
#     -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
#     ftl-container

docker run -p 5000:5000 ftl-container
