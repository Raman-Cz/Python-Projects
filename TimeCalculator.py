def add_time(start, duration,day=""):

    day=day.lower()
    days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

    x=start.split()

    meridian=x[1]
    time_s=x[0].split(":")

    time_d=duration.split(":")

    new_hrs=int(time_s[0])+int(time_d[0])
    new_mins=int(time_s[1])+int(time_d[1])

    if new_mins>=60:
        temp=new_mins
        new_mins=temp%60
        new_hrs+=temp//60
    

    no_of_days=0

    if meridian=="PM":
        x=new_hrs
        no_of_days=x//24
        if x%12==0:
            new_hrs=12
        else:
            new_hrs=x%12
        if x%24<12 :
            meridian="PM"
        else:
            no_of_days+=1
            meridian="AM"
        
    
    else:
        x=new_hrs
        no_of_days=x//24
        if x%12==0:
            new_hrs=12
        else:
            new_hrs=x%12
        if x%24<12 :
            meridian="AM"
        else:
            meridian="PM"
    new_time=str(new_hrs)+":"+"0"*(2-len(str(new_mins)))+str(new_mins)+" "+ meridian

    if no_of_days==0 and day=="":
        return new_time
    if day=="":
        if no_of_days==1:
            new_time+=" (next day)"
        else:
            new_time+=f" ({no_of_days} days later)"
    else:
        idx=days.index(day)
        new_idx=(idx+no_of_days)%7
        new_time+=","+" "+days[new_idx].title()
        if no_of_days==0:
            return new_time
        if no_of_days==1:
            new_time+=" (next day)"
        else:
            new_time+=f" ({no_of_days} days later)"

    return new_time

print(add_time('3:30 PM', '2:12'))