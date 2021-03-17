from requests_html import HTMLSession

url = 'https://tomtkg.github.io/lecture/evaluator1.html?input='
session = HTMLSession()

for i in range(10):
   r = session.get(url + str(i))
   r.html.render()
   output = r.html.find('#output')
   print(str(i) + ': ' + output[0].text)
