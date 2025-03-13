import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(re.sub(r"_", r"-", r"test_76"), "test_76.urls", name="test_76"),
)
