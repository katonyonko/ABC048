from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="048"
#問題
problem="c"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc064_a".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N,x=map(int,input().split())
  A=list(map(int,input().split()))
  ans=max(0,A[0]-x)
  A[0]-=ans
  for i in range(N-1):
    ans+=max(0,A[i+1]+A[i]-x)
    A[i+1]-=max(0,A[i+1]+A[i]-x)
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])