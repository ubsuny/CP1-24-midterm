def years(y):
    years=[i for i in range(1970,y)]
    nyears=[365 for y in years if y%4!=0 or (y%100==0 and y%400!=0)]
    lyears=[366 for y in years if (y%100==0 and y%400==0) or (y%100!=0 and y%4==0)]
    return nyears,lyears

def months_2024():
    """
    months_2024 makes a list of the number of 
    days in each month in 2024. 
    """
    jan=31
    feb=29
    mar=31
    apr=30
    may=31
    jun=30
    jul=31
    aug=31
    sep=30
    octo=31
    nov=30
    dec=31
    return [jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec]

def time(y,m,d,h,mi,s):
    y1_s=(year*86400 for year in years(y)[0])
    y2_s=(year*86400 for year in years(y)[1])
    year_sec=0
    for year in y1_s:
        year_sec+=year
    for year in y2_s:
        year_sec+=year
    months=months_2024()
    count=0
    month_sec=0
    while m-1>count:
        month_sec+=months[count]*86400
        count+=1
    day_sec=(d-1)*86400
    hour_sec=(h+4)*3600
    min_sec=(mi)*60
    sec=s
    return (year_sec+ month_sec+day_sec+hour_sec+min_sec+sec) 

