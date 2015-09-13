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

RUN apk update && apk add python3 && rm -fr /var/cache/apk/*
RUN pip3 install radicale
# Just to be able to use old passwords
RUN pip3 install passlib # needed for apr1
# source: https://github.com/jgehrcke/Radicale/blob/3abbdcf671e2eba13099c7af26927f57a2dfe412/radicale/auth/htpasswd.py
ADD htpasswd.py.with_apr1 /usr/lib/python3.4/site-packages/radicale/auth/htpasswd.py
ADD config /etc/radicale/config
ADD logging /etc/radicale/logging

EXPOSE 5232

CMD [ "/usr/bin/radicale" "-f" ]
