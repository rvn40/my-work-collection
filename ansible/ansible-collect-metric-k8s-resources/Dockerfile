FROM kebonce40/aws-cli:latest

RUN mkdir -p /app && \
    apk update && apk add --no-cache kubectl curl && \
    echo "ansible-playbook pod-cpu-playbook.yaml" > /app/run.sh && \
    chmod +x /app/run.sh

WORKDIR /app

COPY app/ /app/

# Add timezone Jakarta
RUN apk --no-cache --update add tzdata ca-certificates && \
	cp /usr/share/zoneinfo/Asia/Jakarta /etc/localtime && \
	echo "Asia/Jakarta" > /etc/timezone && \
	apk del tzdata

CMD ["/bin/sh", "-c", "/app/run.sh"]