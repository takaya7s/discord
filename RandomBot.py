import discord # インストールした discord.py
import random

client = discord.Client() # 接続に使用するオブジェクト

# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.content.startswith('/random'):
        cmd = message.content.split(" ")
        cmd_cnt = len(cmd)
        
        if cmd_cnt >= 3:
            if cmd[1].isdigit():
                reply = random.randint(int(cmd[1]), int(cmd[2]))
            else:
                reply = cmd[random.randint(1, cmd_cnt - 1]
        elif cmd_cnt == 2:
            reply = random.randint(1, int(cmd[1]))
        else:
            if random.randint(1, 2) == 1:
                reply = "表"
            else:
                reply = "裏"
                                      
        print(reply)
        await client.send_message(message.channel, reply)

# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('NTM5Mzk4NTA4MDI2MDAzNDU3.DzRx5g.rPKTvR0AUOPIpjprF-BvrpVifnw')
