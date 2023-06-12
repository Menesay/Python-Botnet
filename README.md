Educational purposes only.

### Bot and deobfuscated
* bot connects to http server.
* at http server \<body>\</body> should be data like that:
  * 1.1.1.1P80PtcpP10P50Patc
  * P' s for parsing.
  * 1.1.1.1: IP
  * 80: Port
  * tcp: Choice
  * 10: times
  * 50: threads
  * atc: attack (if data is atc attack)

### C2 folder
* c2 folder is another botnet project.
* server.py is very basic c2 server.
* server and bot uses tcp.
* connection is not encrypted.
