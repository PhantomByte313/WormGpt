try:
  import requests
  import LoopAi
except ModuleNotFoundError:
  import os
  os.system("apk add py3-pip")
  os.system("pip install requests")
  os.system("pip install LoopAi==1.0.3")
print(f"""\033[0m

__      __                        _____________________________
/  \    /  \___________  _____    /  _____/\______   \__    ___/
\   \/\/   /  _ \_  __ \/     \  /   \  ___ |     ___/ |    |   
\        (  <_> )  | \/  Y Y  \ \    \_\  \|    |     |    |   
\__/\  / \____/|__|  |__|_|  /  \______  /|____|     |____|   
     \/                    \/          \/                     

Welcome To Worm GPT , The Biggest Enemy of Chat Gpt. By Dark Lord telegram : @ThexDarkxLord

""")



while True:
  worm = LoopAi.Ai()

  w2 = input("Enter your query >>> ")

  response = worm.worm(w2)
  print(response)

