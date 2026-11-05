#!/bin/sh
set -eu
: "${UUID:?UUID environment variable is required}"
WS_PATH="${WS_PATH:-/ray}"
cat > /tmp/xray-config.json <<EOF
{
  "log": { "loglevel": "warning" },
  "inbounds": [
    {
      "port": 3000,
      "protocol": "vless",
      "settings": {
        "clients": [{ "id": "$UUID" }],
        "decryption": "none"
      },
      "streamSettings": {
        "network": "ws",
        "wsSettings": { "path": "$WS_PATH" }
      }
    }
  ],
  "outbounds": [{ "protocol": "freedom" }]
}
EOF
exec /usr/local/bin/xray run -c /tmp/xray-config.json
