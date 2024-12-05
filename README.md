# solvexitydata

Solvexitydata is a data tracker for Crypto Exchanges, e.g. Binance

# Build Kestra dependency

## Prerequisite

```bash
docker login ghcr.io
```


```bash
docker build -t ghcr.io/bullionbear/solvexitydata:binance -f docker/Dockerfile.binance .
docker push ghcr.io/bullionbear/solvexitydata:binance
```

