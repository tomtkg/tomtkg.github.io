from requests_html import HTMLSession

url = "https://tomtkg.github.io/lecture/evaluator2.html?input="
session = HTMLSession()

best_score = -1
best_index = '500'
values = [450, 45, 5]
rank = [100, 10, 1]

for i in range(3):
   base_value = int(best_index) - values[i]
   for j in range(10):
      num = str(j * rank[i] + base_value).zfill(3)
      r = session.get(url + num)
      r.html.render()
      output = r.html.find('#output')
      print(num + ': ' + output[0].text)
      if(best_score < int(output[0].text)):
         best_score = int(output[0].text)
         best_index = num
   print('------------------')

print(best_index + ': ' + str(best_score))
