n = int(input())
input_arr = []
for i in range(n):
  input_arr.append(input())
def extract(log):
  date = log[:10]
  date_num = int((date[:4] + date[5:7] + date[8:10]))
  event = log[20:]
  return tuple((date_num, event))
logs = dict()
for i in input_arr:
  extraction = extract(i)
  if extraction not in logs:
    logs[extraction] = 1
  else:
    logs[extraction] += 1
sorted_arr = list(logs.keys())
sorted_arr.sort(key = lambda x: (x[0], x[1]))
for i in sorted_arr:
  date = str(i[0])[:4] + "-" + str(i[0])[5:7] + str(i[0])[8:10]
  event = i[1]
  count = logs[i]
  print(date, ",",event, ",", count)
