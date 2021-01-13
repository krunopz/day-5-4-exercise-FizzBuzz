#Write your code below this row 👇

#Write all numbers from 1 in 100 in rows, except 
#if the number is divisble by 3 write FIZZ
##if the number is divisble by 5 write BUZZ
#if the number is divisble by 3 and 5 write FIZZBUZZ

for i in range(1,101):
  if i%3==0 and i%5!=0:
    print("Fizz")
  elif i%3!=0 and i%5==0:
    print("Buzz")
  elif i%3==0 and i%5==0:
    print("FizzBuzz")
  else:
    print(i)
