import random
import math
import numpy as np

class Felma:

  def __init__(self, n):
    self.n = n
    self.a = self.random_sampling()
    self.result1 = self.gcd(self.a, self.n)
    self.result2 = self.power_func()

  def random_sampling(self):
    a = random.randrange(2, self.n - 1)
    return a

  def gcd(self, a, b):
    self.GCD = math.gcd(a,b) 
    if self.GCD != 1:
      return '合成数'
    else:
      return ''
  
  # a^(n-1) mod n を計算
  def power_func(self):
    bi = str(format(self.n - 1,"b"))#2進表現に
    self.res = 1
    for i in range(len(bi)):
        self.res = (self.res**2) % self.n
        if bi[i] == "1":
            self.res = (self.res*self.a) % self.n
    if self.res == 1:
      return '素数'
    else:
      return '合成数'

  # a^(n-1)がオーバーフローする場合は　a^(n-1)の計算結果をoverflowとしている
  def __str__(self):
    try:
     str1 = 'a = {}, n = {}\n {}\n gcd(a,n) = {}\n {}\n a^(n-1) = {}\n a^(n-1) mod n = {}\n'.format(
        self.a, self.n, self.result1, self.GCD, self.result2, self.a**(self.n-1), self.res
        )
     return str1

    except OverflowError:
      str1 = 'a = {}, n = {}\n {}\n gcd(a,n) = {}\n {}\n a^(n-1) = {}\n a^(n-1) mod n = {}\n'.format(
        self.a, self.n, self.result1, self.GCD, self.result2, 'overflow', self.res
        )
      return str1

    except ValueError:
      str1 = 'a = {}, n = {}\n {}\n gcd(a,n) = {}\n {}\n a^(n-1) = {}\n a^(n-1) mod n = {}\n'.format(
        self.a, self.n, self.result1, self.GCD, self.result2, 'overflow', self.res
        )
      return str1

def colculate(n):
  with open('result{}.txt'.format(n), 'w') as f:
    for i in range(10):
      f.write('====step{}====\n'.format(i+1))
      f.write(str(Felma(n)))

n = int(input('input n: '))
colculate(n)