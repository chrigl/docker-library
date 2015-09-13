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

FROM debian:latest
MAINTAINER Christoph Glaubitz <chris@chrigl.de>

RUN apt-get -y update && \
  apt-get -y install gcc g++ python-dev libxml2-dev libxslt1-dev libopenjpeg-dev libjpeg62-turbo-dev zlib1g-dev libtiff5-dev

ADD bootstrap.py /opt/plone/bootstrap.py
ADD base.cfg /opt/plone/base.cfg
# disable ssl cert verification
ADD sitecustomize.py /usr/lib/python2.7/
RUN python2.7 /opt/plone/bootstrap.py -c /opt/plone/base.cfg && \
  /opt/plone/bin/buildout -c /opt/plone/base.cfg && \
  useradd -d /opt/plone plone && \
  chown -R plone.plone /opt/plone

ENV PYTHON_EGG_CACHE=/opt/plone/eggs

CMD [ "/opt/plone/bin/instance", "console" ]
