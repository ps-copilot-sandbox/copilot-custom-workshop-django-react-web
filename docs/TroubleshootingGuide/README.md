# Troubleshooting guide

## Problem: You are getting an error port is getting used: docker: Error response from daemon: Ports are not available: listen tcp 0.0.0.0:5432: bind: address already in use.

Terminate the Terminal. Run the following command.

```bash
sudo lsof -i :5432     

sudo kill -9 <PID>
```

## Problem: docker: Error response from daemon: Conflict. The container name "/custom-database-layer" is already in use by container. You have to remove (or rename) that container to be able to reuse that name.

```bash
docker ps -a

docker rm <PS ID>
```

## Problem: My Docker container fails to start. What can I do?

Try to launch image with sh like this:

```bash
docker run -it — rm — entrypoint sh Container Image Name:Container Image Version
```

For example...


```bash
docker run -it — rm — entrypoint sh custom-database-layer:2.0
```

And try to troubleshoot with commands like printenv.
