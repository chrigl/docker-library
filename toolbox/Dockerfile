FROM alpine:latest
MAINTAINER Christoph Glaubitz <chris@chrigl.de>

RUN apk update && \
  apk add tcpdump strace vim vimdiff bash bash-completion && \
  rm -fr /var/cache/apk/*
RUN apk update && \
  apk add openldap-clients mysql-client postgresql-client && \
  rm -fr /var/cache/apk/*
RUN apk update && \
  apk add python3 py-pip && \
  pip3 install ipython ipdb requests && \
  rm -fr /var/cache/apk/*

CMD /bin/bash --login
