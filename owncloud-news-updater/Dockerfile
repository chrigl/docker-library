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

FROM alpine:3.4
MAINTAINER Christoph Glaubitz <chris@chrigl.de>

RUN apk update && \
    apk add python3 ca-certificates && \
    python3 -m ensurepip && \
    rm -fr /var/cache/apk/*
ADD news-updater /news-updater
ADD entrypoint.sh /entrypoint.sh
WORKDIR /news-updater
RUN python3 ./setup.py install --install-scripts=/usr/bin

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "/usr/bin/owncloud-news-updater" ]
