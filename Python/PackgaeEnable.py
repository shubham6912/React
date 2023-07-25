import http.client
import array as arr

a = arr.array('i', [15878,15884,15913,16108,16181,16256,16297,16395,16408,16411,16416,16550,16548,16926,17040,17331,17394,17527,17552,17738,17959,18196,18322,18475,18636,18748,18960,19696,19821,20179,20188,20232,20494,20593,20713,20763,21333,21433,22091])
for x in a:
  payload = 'customerId=:cid&action=true&packageId=103&allDevices=true&packageName=Tag%20Management'
  print(x)
  conn = http.client.HTTPSConnection("url")
  payload=payload.replace(":cid",str(x))

  headers = {
   'authority': 'url',
   'accept': '*/*',
   'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
   'authorization': 'Basic <token>',
   'cache-control': 'no-cache',
   'content-type': 'application/x-www-form-urlencoded',
   'cookie': 'G_AUTHUSER_H=0; JSESSIONID=6C7DD7B295E58CD3A50ECD5B563CAFC3-n1; _ga=GA1.3.1145915837.1685338443; _gcl_au=1.1.567164350.1685338561; _mkto_trk=id:003-XNB-951&token:_mch-azuga.com-1685338561585-76105; calltrk_referrer=https%3A//apps.azuga.com/; calltrk_landing=https%3A//more.azuga.com/fleet-login-promo-1.html; calltrk_session_id=49528ac8-8a3d-46bd-92a4-a9e0aa4b7547; calltrk_fcid=037704b5-e5ef-40b2-b7e6-9b8408aa0a8c; experimentation_subject_id=ImM4MmNkOThjLTliNTAtNDljMS04ZTQ4LWRkMjk5YWEzNjdjNCI%3D--0fa5d28d3643d1d176228894656e7a2daa731b0a; G_ENABLED_IDPS=google; hubspotutk=383d685b5897691d8cbd25f6229237b7; _ga_HXX35F4HRS=GS1.2.1687514763.2.1.1687514781.0.0.0; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=en-US; _lr_uf_-qgonn3=5c80a368-6d01-4247-9e6c-394f004b58fb; oauthToken-apikey=vkIqy85g2x2SIL8Ih4VWaOtzVO7I4ZeU; __hssrc=1; _gid=GA1.2.2003596930.1690184720; AzugaV1=true; p=[object Object]; _gid=GA1.3.2003596930.1690184720; b=1,2,3,4,41,106,113,116,117,124,142,150,155,174,177,178,179,191,192,195,196,200,204,227,232,290,298,300,302,305,314,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,360,361,362,367,377,378,379,380,385,387,389,394,415,416,420,422,427,431,433,437,438,439,440,441,442,443,444,446,447,448,449,450,451,453,454,455,456,459,460,462,464,465,466,467,470,475,476,478,490,495,496,501,502,503; r=42,43,44,45,46,48,49,51,60,61,62,76,81,82,83,100,134,173,276,283,288,289,292,294,299,313,317,323,325,326,327,369,374,390,418,421,435,436,457,484,488,493,494; _ga_LTEVWT33K1=GS1.1.1690278259.131.0.1690278259.60.0.0; _ga=GA1.1.1738941736.1685338561; _uetsid=9c0ab3f029fc11ee810c376250bbcb6d; __hstc=238852191.383d685b5897691d8cbd25f6229237b7.1685941869736.1690187545260.1690278261215.54; __hssc=238852191.1.1690278261215; Pod=NODE_1; _ga_XG0ZWQ17WE=GS1.1.1690278256.83.1.1690278302.0.0.0; isV1Active=true; u=undefined; nodeName=NODE_1; _lr_tabs_-qgonn3%2Ffleet-web-production={%22sessionID%22:0%2C%22recordingID%22:%225-4668f8a0-6232-4170-80b6-4284c164f5eb%22%2C%22webViewID%22:null%2C%22lastActivity%22:1690278972690}; _lr_hb_-qgonn3%2Ffleet-web-production={%22heartbeat%22:1690278972691}; oauthToken-apikey=JMklUhmfWlxGTong3t5ZRje1pLqQP54U; _ga_XG0ZWQ17WE=GS1.3.1690278256.83.1.1690278974.0.0.0',
   'origin': 'url',
   'pragma': 'no-cache',
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