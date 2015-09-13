# Copyright 2015 Christoph Glaubitz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM alpine:latest
MAINTAINER Christoph Glaubitz <chris@chrigl.de>

RUN apk update && apk add gcc musl-dev python libxml2-dev libxslt-dev openjpeg-dev libjpeg-turbo-dev zlib-dev tiff-dev && rm -fr /var/cache/apk/*
ADD bootstrap.py /opt/plone/bootstrap.py
ADD base.cfg /opt/plone/base.cfg
# disable ssl cert verification
ADD sitecustomize.py /usr/lib/python2.7/
RUN python2.7 /opt/plone/bootstrap.py -c /opt/plone/base.cfg && \
  /opt/plone/bin/buildout -c /opt/plone/base.cfg && \
  adduser -D plone -h /opt/plone && \
  chown -R plone.plone /opt/plone

ENV PYTHON_EGG_CACHE=/opt/plone/eggs

CMD [ "/opt/plone/bin/instance", "console" ]
