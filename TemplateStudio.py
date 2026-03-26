# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:14:20 2026

@author: ShiLn
"""
import os
import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime, timedelta

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

MAPS = ["SPLIT", "BIND", "HAVEN", "LOTUS", "FRACTURE", "PEARL", "BREEZE"]

SIDES = ["def vs att", "att vs def"]

# 日期快速選擇
def get_date(option):
    today = datetime.now()
    if option == "today":
        return today.strftime("%m/%d")
    elif option == "tomorrow":
        return (today + timedelta(days=1)).strftime("%m/%d")
    return option  # 自訂輸入

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"登入成功：{bot.user}")

# ====================
# 模板一
# ====================
@bot.tree.command(name="scrim1")
@app_commands.describe(
    date="日期 (today / tomorrow 或自己打 3/26)",
    time="時間",
    maps="幾張圖（預設2）",
    rounds="幾回合（預設24）"
)
async def scrim1(interaction: discord.Interaction, date: str, time: str, maps: int = 2, rounds: int = 24):

    date = get_date(date)

    text = f"""•••´º´•» 𝐋𝐨𝐨𝐤𝐢𝐧𝐠 𝐟𝐨𝐫 𝐬𝐫𝐢𝐦 «•´º´•••

𝑻𝒆𝒂𝒎：𝑫𝑻𝑮(𝑮𝑪)
𝑹𝒂𝒏𝒌：𝒂𝒔𝒄~𝒊𝒎𝒎𝒐
𝑺𝒆𝒓𝒗𝒆𝒓：𝑯𝑲
𝑫𝒂𝒕𝒆：{date}
𝑻𝒊𝒎𝒆：{time}
𝑻𝒚𝒑𝒆：{maps}map {rounds}r｜𝑪𝑶𝑨𝑪𝑯 ✓ 𝑶𝑩 ✘

𝑷𝒍𝒆𝒂𝒔𝒆 𝑫𝑴 𝒎𝒆 𝒘𝒊𝒕𝒉 𝒕𝒆𝒂𝒎 𝒏𝒂𝒎𝒆 & 𝒓𝒂𝒏𝒌 𝒕𝒉𝒂𝒏𝒌𝒔
"""
    await interaction.response.send_message(text)

# ====================
# 模板二（重點🔥）
# ====================
@bot.tree.command(name="scrim2")
@app_commands.describe(
    opponent="對手名稱",
    date="today / tomorrow / 自訂",
    time="時間",
    map1="第一場地圖",
    map2="第二場地圖",
    side1="第一場攻守（預設: def vs att）",
    side2="第二場攻守（預設: def vs att）",
    maps="幾張圖",
    rounds="幾回合"
)
@app_commands.choices(
    map1=[app_commands.Choice(name=m, value=m) for m in MAPS],
    map2=[app_commands.Choice(name=m, value=m) for m in MAPS],
)
async def scrim2(
    interaction: discord.Interaction,
    opponent: str,
    date: str,
    time: str,
    map1: app_commands.Choice[str],
    map2: app_commands.Choice[str],
    side1: str = "不影響（𝚍𝚎𝚏 𝚟𝚜 𝚊𝚝𝚝）",
    side2: str = "不影響（𝚍𝚎𝚏 𝚟𝚜 𝚊𝚝𝚝）",
    maps: int = 2,
    rounds: int = 24
):
    date = get_date(date)

    text = f"""• 隊伍｜DTG vs {opponent}
    • 日期｜{date}
    • 時間｜{time}
    • 賽制｜{maps}map {rounds}r
    • 排位｜immo+
    • 伺服器｜HK
    • coach ✓   OB ✘
    
    > **第一場**
    > 地圖：{map1.value}
    > 攻守方：{side1}
    
    > **第二場**
    > 地圖：{map2.value}
    > 攻守方：{side2}
    """
    await interaction.response.send_message(text)

# ====================
# 模板三
# ====================
@bot.tree.command(name="scrim3")
@app_commands.describe(
    opponent="對手隊伍名稱",
    date="日期 (3/26)",
    time="時間 (20:00)",

    ban_a1="Team A 第一Ban",
    ban_b1="Team B 第一Ban",

    map1="第一張地圖",
    map2="第二張地圖",

    ban_a2="Team A 第二Ban",
    ban_b2="Team B 第二Ban",

    decider="決勝圖",

    map1_att="第一張 ATT",
    map2_att="第二張 ATT",
    map3_att="決勝圖 ATT"
)
@app_commands.choices(
    ban_a1=[app_commands.Choice(name=m, value=m) for m in MAPS],
    ban_b1=[app_commands.Choice(name=m, value=m) for m in MAPS],
    map1=[app_commands.Choice(name=m, value=m) for m in MAPS],
    map2=[app_commands.Choice(name=m, value=m) for m in MAPS],
    ban_a2=[app_commands.Choice(name=m, value=m) for m in MAPS],
    ban_b2=[app_commands.Choice(name=m, value=m) for m in MAPS],
    decider=[app_commands.Choice(name=m, value=m) for m in MAPS],

    map1_att=[
        app_commands.Choice(name="Team A", value="A"),
        app_commands.Choice(name="Team B", value="B"),
    ],
    map2_att=[
        app_commands.Choice(name="Team A", value="A"),
        app_commands.Choice(name="Team B", value="B"),
    ],
    map3_att=[
        app_commands.Choice(name="Team A", value="A"),
        app_commands.Choice(name="Team B", value="B"),
    ],
)
async def scrim3(
    interaction: discord.Interaction,
    opponent: str,
    date: str,
    time: str,

    ban_a1: app_commands.Choice[str],
    ban_b1: app_commands.Choice[str],

    map1: app_commands.Choice[str],
    map2: app_commands.Choice[str],

    ban_a2: app_commands.Choice[str],
    ban_b2: app_commands.Choice[str],

    decider: app_commands.Choice[str],

    map1_att: app_commands.Choice[str],
    map2_att: app_commands.Choice[str],
    map3_att: app_commands.Choice[str],
):
    teamA = "DTG(GC)"
    teamB = opponent

    def get_side(att_choice):
        if att_choice.value == "A":
            return teamA, teamB
        else:
            return teamB, teamA

    att1, def1 = get_side(map1_att)
    att2, def2 = get_side(map2_att)
    att3, def3 = get_side(map3_att)

    text = f"""𝐃𝐓𝐆(𝐆𝐂) 𝐯𝐬 {teamB}
𝐃𝐚𝐭𝐞 : {date}
𝐓𝐢𝐦𝐞 : {time}

𝐓𝐞𝐚𝐦 𝐀 - {teamA}
𝐓𝐞𝐚𝐦 𝐁 - {teamB}

𝐓𝐞𝐚𝐦 𝐀 𝟏𝐬𝐭 𝐁𝐚𝐧 - {ban_a1.value}
𝐓𝐞𝐚𝐦 𝐁 𝟏𝐬𝐭 𝐁𝐚𝐧 - {ban_b1.value}

𝟏𝐬𝐭 𝐌𝐀𝐏 (𝐓𝐞𝐚𝐦 𝐀) : {map1.value}
𝐀𝐓𝐓: {att1}
𝐃𝐄𝐅: {def1}

𝟐𝐧𝐝 𝐌𝐀𝐏 (𝐓𝐞𝐚𝐦 𝐁) : {map2.value}
𝐀𝐓𝐓: {att2}
𝐃𝐄𝐅: {def2}

𝐓𝐞𝐚𝐦 𝐀 𝟐𝐧𝐝 𝐁𝐚𝐧 : {ban_a2.value}
𝐓𝐞𝐚𝐦 𝐁 𝟐𝐧𝐝 𝐁𝐚𝐧 : {ban_b2.value}

𝐃𝐞𝐜𝐢𝐝𝐞𝐫 𝐌𝐚𝐩: {decider.value}
𝐀𝐓𝐓: {att3}
𝐃𝐄𝐅: {def3}

這邊是時程表，有需要取消再幫我提前30分鐘告知，遲到我們是保留15分鐘的時間，超過了就當下在跟我的隊員商議是否繼續就好，謝謝你們
"""

    await interaction.response.send_message(text)

bot.run(os.getenv("DISCORD_TOKEN"))