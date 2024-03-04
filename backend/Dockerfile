FROM python:3.9-alpine3.13
LABEL maintainer="Jimoh Muhammed"

# ENV PYTHONNUMBERBUFFERED 1

ENV PYTHONUNBUFFERED 1
ENV PATH="/scripts:${PATH}"

RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /apps
WORKDIR /apps
COPY ./apps /apps
COPY ./scripts/ /scripts/
RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN chmod -R 755 /vol/web


# USER django-user

CMD [ "run.sh" ]