import requests as req
res = req.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
res.raise_for_status()
data = res.json()
# print(data)
question_data = data['results']
# print(question_data)
