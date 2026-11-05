# xray-cloady

Xray VLESS + WebSocket 节点，跑在 Cloady 免费试用上。

- 多阶段 Dockerfile：第一阶段用官方 `ghcr.io/xtls/xray-core` 镜像（无 shell）只取 `/usr/local/bin/xray` 二进制，第二阶段拷进 Alpine 运行。
- 容器内监听 3000 端口（VLESS + WS，明文，TLS 由 Cloady 边缘自动 HTTPS 终止），对外 443。
- UUID 不写进仓库：部署时在 Cloady 里设环境变量 `UUID`（`WS_PATH` 可选，默认 `/ray`）。

部署：Cloady 里新建应用 → 粘贴本仓库地址 → Build 根目录填 `xray-cloady` → 区域选 `usw1` → 服务端口 `3000` → 资源不超过 0.5 vCPU / 1 GB / 5 GB → 环境变量 `UUID` → Deploy。
