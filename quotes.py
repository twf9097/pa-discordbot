from models import Quote, Session
from discord.ext import commands
from sqlalchemy import desc
import random
import typing

session = Session()

class Quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx, number: typing.Optional[int]):
        q = None
        server = ctx.guild.id
        if number:
            q = session.query(Quote).filter(Quote.number == number, Quote.server == server).one()
            if q is none: return
        else:
            q = random.choice(session.query(Quote).filter(Quote.server==server).all())
        await ctx.send(q.message)
    
    @commands.command()
    async def addquote(self, ctx, message_id):
        m = await ctx.channel.fetch_message(message_id)
        if m.guild.id == ctx.guild.id:
            q = Quote()
            q.author = m.author.id
            q.message = m.content
            q.time_sent = m.created_at
            q.server = m.guild.id
            q.added_by = ctx.author.id
            highest = session.query(Quote).filter(Quote.server==ctx.guild.id).order_by(desc(Quote.id)).first()
            q.number = highest.number+1 if highest else 1
            session.add(q)
            session.commit()
            await ctx.send("added")



