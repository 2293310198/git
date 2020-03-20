import requests

import time

for i in range(1, 101):

 with open('img\{}.png'.format(i), 'wb') as f:

  time.sleep(0.1)

  f.write(requests.get('https://cas.baidu.com/?action=image&key=1550211305&random=1550213601085').content)

  print('成功获取一张验证码')
