FROM haproxy:1.9.4

RUN mkdir -p /var/lib/haproxy
RUN mkdir -p /run/haproxy
COPY haproxy.cfg /etc/haproxy/haproxy.cfg

CMD ["haproxy", "-f", "/etc/haproxy/haproxy.cfg"]
