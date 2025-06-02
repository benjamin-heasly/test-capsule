# hash:sha256:c2ad9650ecee57f1ddd712ff98dbbdf9a3ad1a6174dc2af256e4724def70c149
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/mambaforge3:24.5.0-0-python3.12.4-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

ENV MESSAGE=hello_world
