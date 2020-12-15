import sys

sys.path.append("../")
from send_request import send_request
import config

# test rfc7230 section 5.4 Host


def test_proxy() -> str:
    request_header = "GET /proxy HTTP/1.1\r\nHost: xxx\r\n\r\n"
    http_response = send_request(request_header)
    if http_response.status == 400:
        return "Bad status code: {}, expected: {}".format(
            str(http_response.status), "400"
        )
    body = http_response.read().decode("UTF-8")
    if body.find("If you see this the proxy is working!") == -1:
        return "Bad content: expected to find 'If you see this the proxy is working!'"
    return ""


def test_regex() -> str:
    request_header = "GET /regex/hello.txt HTTP/1.1\r\nHost: xxx\r\n\r\n"
    http_response = send_request(request_header)
    if http_response.status == 400:
        return "Bad status code: {}, expected: {}".format(
            str(http_response.status), "400"
        )
    body = http_response.read().decode("UTF-8")
    if body.find("if you see this the regex is working") == -1:
        return "Bad content: expected to find 'if you see this the regex is working'"
    return ""
