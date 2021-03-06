import speedtest
s = speedtest.Speedtest()
s.get_best_server()
s.download()
s.upload()
res = s.results.dict()
upload_speed = round(res["upload"]/1000000, 1)
download_speed = round(res["download"]/1000000, 1)
ping = int(res["ping"])
print(f"Download speed: {download_speed} mbit/s; Upload speed: {upload_speed} mbit/s; Ping: {ping} ms")