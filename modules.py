# own modules
# thirdy party modules
# python modules

#import datetime

#from datetime import timedelta, date

#print(datetime.date.today())
#print(datetime.timedelta(minutes=100))

#print(date.today())




import funt_match
 funt_match.add(1,2)
 funt_match.substract(1,2)

 from funt_match import add, substract
 add(1,3)
 substract(1,3)




from colorama import Fore, Back, Style, init
init(convert = True)

print(Fore.RED + "Hello world")