from sqlalchemy import Column, String, create_engine,Integer,BigInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()	
class Prize(Base):
    # 表的名字:
    __tablename__ = 'prize'	
    # 表的结构:
    prize_id = Column(Integer, primary_key=True)
    pool = Column(BigInteger)
    sale = Column(Integer)
    red_1 = Column(String(2))
    red_2 = Column(String(2))
    red_3 = Column(String(2))
    red_4 = Column(String(2))
    red_5 = Column(String(2))	
    red_6 = Column(String(2))
    blue = Column(String(2))
    prize_time = Column(String(10))	
    prize_num_1 = Column(Integer)
    per_prize_money_1 = Column(Integer)
    prize_num_2 = Column(Integer)
    per_prize_money_2 = Column(Integer)
    prize_num_3 = Column(Integer)
    per_prize_money_3 = Column(Integer)
    prize_num_4 = Column(Integer)
    per_prize_money_4 = Column(Integer)
    prize_num_5 = Column(Integer)
    per_prize_money_5 = Column(Integer)
    prize_num_6 = Column(Integer)
    per_prize_money_6 = Column(Integer)
	
    def __str__(self):
        return ('prize_id: {prize_id},'
        'pool:{pool},'	
        'sale:{sale},'	
        'red_1:{red_1},'	
        'red_2:{red_2},'
        'red_3:{red_3},'
        'red_4:{red_4},'
        'red_5:{red_5},'
        'red_6:{red_6},'	
        'blue:{blue},'
        'prize_time:{prize_time},'
        'prize_num_1:{prize_num_1},'
        'per_prize_money_1:{per_prize_money_1},'
        'prize_num_2:{prize_num_2},'
        'per_prize_money_2:{per_prize_money_2},'
        'prize_num_3:{prize_num_3},'
        'per_prize_money_3:{per_prize_money_3},'
        'prize_num_4:{prize_num_4},'
        'per_prize_money_4:{per_prize_money_4},'
        'prize_num_5:{prize_num_5},'
        'per_prize_money_5:{per_prize_money_5},'
        'prize_num_6:{prize_num_6},'
        'per_prize_money_6:{per_prize_money_6}'		
        ).format(**self.__dict__)
    def __repr__(self):
       return self.__str__()

	
def dict2Prize(d):
	prize=Prize()
	prize.prize_id = int(d['id'])
	prize.pool = int(d.get('pool','0'))
	prize.sale = int(d.get('sale','0'))
	prize.prize_time = d.get('time','1997-01-01').split(' ')[0]
	matchball = d.get('matchball','')
	balls = matchball.split(' ')
	if len(balls) == 7:
		prize.red_1 = balls[0]
		prize.red_2 = balls[1]
		prize.red_3 = balls[2]
		prize.red_4 = balls[3]
		prize.red_5 = balls[4]
		prize.red_6 = balls[5]
		prize.blue = balls[6]
	bounesStr = d.get('bonus','')
	bounesList = bounesStr.split('|')
	for boune in bounesList:
		setPirzeNumAndMoney(prize,boune)
	return prize

def setPirzeNumAndMoney(prize,boune):
	blist = boune.split(',')
	if len(blist) == 3:
		if blist[0] == '一等奖':
			prize.prize_num_1=int(blist[1])
			prize.per_prize_money_1=int(blist[2])
		elif blist[0] == '二等奖':
			prize.prize_num_2=int(blist[1])
			prize.per_prize_money_2=int(blist[2])
		elif blist[0] == '三等奖':
			prize.prize_num_3=int(blist[1])
			prize.per_prize_money_3=int(blist[2])
		elif blist[0] == '四等奖':
			prize.prize_num_4=int(blist[1])
			prize.per_prize_money_4=int(blist[2])
		elif blist[0] == '五等奖':
			prize.prize_num_5=int(blist[1])
			prize.per_prize_money_5=int(blist[2])
		elif blist[0] == '六等奖':
			prize.prize_num_6=int(blist[1])
			prize.per_prize_money_6=int(blist[2])