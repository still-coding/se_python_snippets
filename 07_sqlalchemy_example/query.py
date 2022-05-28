from config import DATABASE_URI
from model import Corresp, Type, Department, External
from crud import get_session_engine
import matplotlib.pyplot as plt

s, _ = get_session_engine(DATABASE_URI)

qry = s.query(Corresp, Type, Department, External)\
.filter(Corresp.type_id == Type.id)\
.filter(Corresp.internal_id == Department.id)\
.filter(Corresp.external_id == External.id)

print(qry.statement)

query_res = qry.all()


query_dict = {}

for q in query_res:
    month = q.Corresp.date.month
    if month in query_dict:
        query_dict[month].append(q)
    else:
        query_dict[month] = [q]


for m in range(1, 13):
    if m in query_dict:
        print(m, 'месяц')
        for c in query_dict[m]:
            print(f'\t{c.Corresp.date} {c.Type}: {c.Corresp.subject}')


plt.bar(query_dict.keys(), [len(c) for c in query_dict.values()])
plt.show()
