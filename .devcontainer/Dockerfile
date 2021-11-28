FROM golang:1.15.6

RUN apt update \
    && apt install -y vim

ENV GO111MODULE on
WORKDIR /go/src/work

# install go tools
RUN go get golang.org/x/tools/gopls