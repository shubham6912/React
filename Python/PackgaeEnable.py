import http.client
import array as arr

a = arr.array('i', [15878,15884,15913,16108,16181,16256,16297,16395,16408,16411,16416,16550,16548,16926,17040,17331,17394,17527,17552,17738,17959,18196,18322,18475,18636,18748,18960,19696,19821,20179,20188,20232,20494,20593,20713,20763,21333,21433,22091])
for x in a:
  print(x)
  conn = http.client.HTTPSConnection("url")
  payload=payload.replace(":cid",str(x))

  headers = {
   'authority': 'url',
   'accept': '*/*',
   'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
   'authorization': 'Basic <token>',
   'cache-control': 'no-cache',
   'referer': 'url/supportportal.html?l=en_US',
   'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
   'sec-ch-ua-mobile': '?0',
   'sec-ch-ua-platform': '"macOS"',
   'sec-fetch-dest': 'empty',
   'sec-fetch-mode': 'cors',
   'sec-fetch-site': 'same-origin',
   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
   'x-requested-with': 'XMLHttpRequest'
  }
  conn.request("POST", "url", payload, headers)
  res = conn.getresponse()
  data = res.read()
  print(data.decode("utf-8"))  