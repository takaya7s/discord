import discord # インストールした discord.py
import random

client = discord.Client() # 接続に使用するオブジェクト

# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')

# 「/neko」と発言したら「にゃーん」が返る処理
@client.event
async def on_message(message):
    if message.content.startswith('/random'):
        cmd = message.content.split(" ")
        if len(cmd) == 3:
            reply = random.randint(int(cmd[1]), int(cmd[2]))
        elif len(cmd) == 2:
            reply = random.randint(1, int(cmd[1]))
        else:
            reply = "構文は　/random 最小数 最大数　もしくは　/random 最大数　です"
        print(reply)
        await client.send_message(message.channel, reply)

# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('NTM5Mzk4NTA4MDI2MDAzNDU3.DzRx5g.rPKTvR0AUOPIpjprF-BvrpVifnw')