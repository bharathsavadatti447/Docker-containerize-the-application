FROM python:3.10-slim
ARG APP_HOME=/python-app
ARG APP_USER=webuser
ENV PORT=8000 \
    APP_ENV=development \
    PYTHONUNBUFFERED=1
RUN apt-get update && \
	apt-get install -y curl && \
	useradd -m ${APP_USER}

WORKDIR ${APP_HOME}
COPY server.py ${APP_HOME}/
EXPOSE ${PORT}
USER ${APP_USER}
ENTRYPOINT ["python"]
CMD ["server.py"]
