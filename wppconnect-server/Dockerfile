FROM node:lts-alpine3.18 AS builder

ENV PORT=21465

RUN apk add wget && \
    apk add --no-cache git

WORKDIR /home/node
RUN git clone https://github.com/wppconnect-team/wppconnect-server.git /home/node/app 

WORKDIR /home/node/app

# COPY ./config.ts /home/node/app/src

RUN yarn install
RUN yarn build


FROM node:lts-alpine3.18
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
WORKDIR /home/node/app
RUN apk add chromium
COPY --from=builder /home/node/app/ .
EXPOSE 21465

RUN yarn add sharp --ignore-engines
RUN apk update && \
    apk add --no-cache \
    vips-dev \
    fftw-dev \
    gcc \
    g++ \
    make \
    libc6-compat \
    && rm -rf /var/cache/apk/*

ENTRYPOINT ["node", "dist/server.js"]