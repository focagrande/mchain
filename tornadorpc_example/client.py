from jsonrpclib import Server
server = Server('http://localhost:8080')
result = server.tree.power(2, 6)

print result
