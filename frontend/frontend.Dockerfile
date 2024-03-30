# my-react-app/Dockerfile
FROM node:14-alpine


COPY package*.json ./

RUN npm install

RUN npm install @mui/material @mui/styled-engine-sc styled-components
RUN npm install @fontsource/roboto
RUN npm install @mui/icons-material

RUN npm install @emotion/react @emotion/styled

COPY ./ .

CMD ["npm", "start"]
