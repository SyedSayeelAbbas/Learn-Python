#you can take a portion of an string by using slicig which need a satrting index the protion you want to start taking
#and a ending index the protion you want to end Like
a="Sayeel"
#i want a to l
print(a[1:5+1])
#i add plus 1 as ending index is always skipped so you but starting index is included
#use following method if you want
print(a[1:len(a)])#len always start from 1 but indexing start from 0
#We can also use negative value for slicing 
#S=-6,a=-5,y=-4,e=-3,e=-2,l=-1
print(a[-5:-1])