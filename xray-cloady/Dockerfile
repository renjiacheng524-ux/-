# Stage 1: official Xray image has no shell - use it only to extract the binary
FROM ghcr.io/xtls/xray-core:latest AS xray

# Stage 2: Alpine runtime (has /bin/sh)
FROM alpine:latest
RUN apk add --no-cache ca-certificates
COPY --from=xray /usr/local/bin/xray /usr/local/bin/xray
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 3000
ENTRYPOINT ["/entrypoint.sh"]
