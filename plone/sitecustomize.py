# http://legacy.python.org/dev/peps/pep-0476/
# disable certificate validation by default
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
