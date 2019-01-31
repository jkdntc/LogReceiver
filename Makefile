EDITOR=vim

all: regconfig build

build:
	docker build -t jiangkun/logreceiver .

run: build
	docker run -ti --privileged -v /sys/fs/cgroup:/sys/fs/cgroup -v /run -v /etc/hosts:/etc/hosts:ro -p 8082:8080 jiangkun/logreceiver


clean:
	docker system prune
	
prune:
	docker system prune -f

exec:
	docker exec -ti `docker ps | grep jiangkun/logreceiver |head -1 | awk -e '{print $$1}'` /bin/bash

stop:
	docker stop `docker ps | grep jiangkun/logreceiver |head -1| awk -e '{print $$1}'`

