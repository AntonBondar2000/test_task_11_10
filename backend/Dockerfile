FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /srv/project
WORKDIR /srv/project
COPY . /srv/project
RUN pip install --no-cache-dir -r /srv/project/requirements.txt
EXPOSE 8081
