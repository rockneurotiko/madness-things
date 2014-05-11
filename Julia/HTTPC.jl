using HTTPClient.HTTPC

#Mas aqui: http://pili.la/aaacq
r = HTTPC.get("http://www.google.es")

println(bytestring(r.body))
println("Status:", r.http_code)
println("time_exec:", r.total_time)
println("Headers:", r.headers)
