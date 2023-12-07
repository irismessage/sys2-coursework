import telnetlib


with telnetlib.Telnet("192.168.100.1", port=80) as tn:
    for line in (
        b"POST /cgi-bin/hello-post.cgi?first_name=Bob&last_name=jm3017 HTTP/1.1\r\n",
        b"Host: Ubuntu1\r\n",
        b"\r\n",
    ):
        tn.write(line)
    response = tn.read_until(b"</html>")

response = response.decode("utf-8")
print(response)
