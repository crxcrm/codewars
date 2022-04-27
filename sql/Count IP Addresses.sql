-- Given a database of first and last IPv4 addresses, calculate the number of addresses between them (including the first one, excluding the last one).

SELECT id, last::inet - first::inet AS ips_between
FROM ip_addresses;
