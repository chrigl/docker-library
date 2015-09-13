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

FROM chrigl/plone-debian:4.3.6
MAINTAINER Christoph Glaubitz <chris@chrigl.de>

RUN apt-get -y update && apt-get -y install libgeos-dev
ADD buildout.cfg /opt/plone/buildout.cfg
ADD src/ /opt/plone/src/
RUN /opt/plone/bin/buildout -N -c /opt/plone/buildout.cfg
