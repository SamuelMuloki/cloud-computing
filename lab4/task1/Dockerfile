# This tutorial is for lab5 session
FROM alpine
RUN apk add --update nodejs npm
WORKDIR /app
COPY . /app
RUN npm install
EXPOSE 3000
CMD ["node", "index.js"]