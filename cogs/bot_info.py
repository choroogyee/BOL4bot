import discord
from discord.ext import commands
import asyncio
import datetime
from datetime import date
import time
import bs4
from urllib.request import urlopen, Request
import urllib
import urllib.request
import random

intents = discord.Intents.default()
intents.members = True
botname = 'BOL4봇'
uptime = time.time()

class bot_info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="정보")
    async def info(self, ctx):
        end = time.time()-uptime
        ut = int(end)
        min = int(ut/60)
        hour = int(min/60)
        day = str(int(hour/24))
        hour = str(hour%24)
        ut = str(ut%60)
        min = str(min%60)
        e=discord.Embed(title='BOL4봇의 정보', description='BOL4봇의 정보입니다.', color=0xffc0cb)
        e.add_field(name='업타임', value=day+'일 '+hour+'시간 '+min+'분 '+ut+'초', inline=True)
        e.add_field(name='Since', value='2021년 7월 4일', inline=True)
        e.add_field(name='자료 출처', value='나무위키 볼빨간사춘기, 안지영, 우지윤 문서', inline=True)
        e.add_field(name='개발자', value='초롱이#3632', inline=False)
        e.add_field(name='봇이름', value=botname, inline=True)
        e.set_thumbnail(url='https://i.ibb.co/4YfRj8r/profile.jpg')
        e.set_footer(text='%s#%s' % (ctx.message.author.name, ctx.message.author.discriminator), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=e)
        print('%s#%s님이 BOL4봇 정보를 확인하였습니다.' % (ctx.message.author.name, ctx.message.author.discriminator))

    @commands.command(name="기능문의", aliases=['문의'])
    async def contact(self, ctx):
        e=discord.Embed(title='기능문의는 여기에!', description='기능뿐만 아니라 오류 제보도 부탁드려요.', color=0xffc0cb)
        e.add_field(name='개발자 디스코드', value='초롱이#3632', inline=False)
        e.add_field(name='개발자 카카오톡', value='Love_Bol4', inline=False)
        e.add_field(name='개발자 개인 페이스북', value='https://facebook.com/bakbugeun', inline=False)
        e.add_field(name='개발자 이메일', value='pbk050207@kakao.com', inline=False)
        e.set_footer(text='%s#%s' % (ctx.message.author.name, ctx.message.author.discriminator), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=e)
        await ctx.send(':warning: 해당 개인정보를 기능문의나 오류제보가 아닌 타 목적으로 사용할 경우 법적으로 처벌받을수 있음을 안내드립니다. ')
        print('%s#%s님이 기능을 문의하였거나 오류를 제보하였습니다.' % (ctx.message.author.name, ctx.message.author.discriminator))

def setup(bot: commands.Bot):
    bot.add_cog(bot_info(bot)) 