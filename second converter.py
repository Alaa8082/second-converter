
def sectime(a):

	years = a / 31104000 # number of years

	if a%31104000 !=0:
		MonthInSec = a - (31104000*years) # number of months in second 
		month = MonthInSec / 2592000 # number of months
	else:
		print  years , " y : " , "0" , " m : " , "0" , " d : " , "0" , " h : " , "0"  , " min : " , "0" , " s "
	if MonthInSec% 2592000 !=0:
		DaysInSecond = MonthInSec - (2592000*month) # number of days in second
		days = DaysInSecond / 86400
	else:
		print  years , " y : " , month , " m : " , "0" , " d : " , "0" , " h : " , "0"  , " min : " , "0" , " s "
	if  DaysInSecond %86400 !=0:
		HoursInSec = DaysInSecond - (86400*days)
		hours = HoursInSec / 3600
	else:
		print  years , " y : " , month , " m : " , days , " d : " , "0" , " h : " , "0"  , " min : " , "0" , " s "
	if  HoursInSec %3600 != 0:
		MinInSecd = HoursInSec - (3600*hours)
		mintes = 	MinInSecd / 60	
	else:
		print  years , " y : " , month , " m : " , days , " d : " , hours , " h : " , "0"  , " min : " , "0" , " s "
	if  MinInSecd %60 !=0:
		seconds = MinInSecd - (60*mintes)
		print  years , " y : " , month , " m : " , days , " d : " , hours , " h : " , mintes  , " min : " , seconds , " s "
	



print sectime(839808600)
