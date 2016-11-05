#!/bin/sh

: ${OWNCLOUD_USER:=admin}
: ${OWNCLOUD_PASS:=admin}
: ${OWNCLOUD_URL:=http://localhost/owncloud}

if [ "$1" = "/usr/bin/owncloud-news-updater" ]; then
	exec "$@" -u $OWNCLOUD_USER -p $OWNCLOUD_PASS $OWNCLOUD_URL
fi

exec "$@"
