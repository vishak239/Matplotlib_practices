import matplotlib.pyplot as plt

# Line plot
"""
Name = ["Apple","Mango","Orange"]
Price = [280,190,180]
plt.plot(Name,Price,color="Green",linestyle=":",marker="+")
plt.xlabel("Name")
plt.ylabel("price")
plt.title("Fruits")
plt.show()"""


#Scatter plot

"""Emp_name = ["Raj","Jhon","Ancy","Bellavita","Arron"]
Emp_salary = [2000,25000,40000,35000,50000]
plt.scatter(Emp_name,Emp_salary,color = "Red",linestyle="",marker="o",cmap="magma",edgecolor="Black")
plt.colorbar(label="color intensity")
plt.xlabel("Emp_salary")
plt.ylabel("Emp_name")
plt.title("Emp Salary datas")
plt.show ()"""

#Pie chart


"""Name=["vishak","vidya","Lalitha","vincent"]
Age=[21,27,45,50]
size=(30,45,50,32)
mycolor=["red","Purple","lavender","indigo"]
plt.pie(size,labels=Name,shadow=True,colors=mycolor,startangle=90)
plt.legend()
plt.title("AGE")
plt.show()"""

#Box plot

"""box1 = [1,3,6,9,12,15,18,21,24,27,30]
box2 = [10,60,50,45,23,6,89,100,23,67,23]
plt.boxplot([box1,box2],labels=["Raju","Ram"])
plt.title("Box plot")

plt.show()"""

#Histogram

"""Product = ["Shirts","Pants","Shoes","Sunglasses","Waist bag","Rings","Chain","Watches"]
price = [800,1500,1500,2000,250,200,250,2500]

plt.hist(price,bins=8,color="purple",edgecolor="Black",alpha=0.7)

plt.xlabel("product")
plt.ylabel("price")
plt.title("List")
plt.legend()
plt.show()"""

#Bar chart

"""product = ["Apple","Orange","Mango","Lemon","Banana","Grapes","Strawberry","gova"]
price = [200,345,120,380,20,250,180,250]
colors = ["red","blue","green","orange","purple","pink","cyan","yellow"]
plt.bar(product,price,color=colors,edgecolor="Black")
plt.xlabel("product")
plt.ylabel("price")
plt.title("PRODUCTS LIST")

plt.xticks(rotation=30)
plt.show()"""

#Multiple lines

"""Sports = ["Badmin","Cricket","Football","Disk_throw","Volley ball","Long jump"]
No_ply = [2,11,11,1,12,1]
year = [1997,1998,1992,1996,1999,2001]
plt.plot(No_ply,year,label="Sports",color="darkblue",linestyle="-.",marker="o")
plt.plot(Sports,year,label="No_years",color="darkgreen",linestyle=":",marker="+")
plt.title("comparison")
plt.xlabel("Sports Name")
plt.ylabel("Year")
plt.xticks(rotation=25)
plt.show()"""


#Horizondal bar chart

"""Name = ["Avenger","Wonka","Bet","Years later"]
Movie_price=[200,180,100,200]
colors=["red","darkblue","darkgreen","purple"]
plt.barh(Name,Movie_price,color=colors,edgecolor="Black")
plt.title("MOVIE_LIST")
plt.xlabel("Name")
plt.ylabel("Movie_name")
plt.yticks(rotation=30)
plt.xticks(rotation=30)
plt.show()"""


#Sub plot


"""Games = ["Black myth","RDR","COD","F1"]
users = [300,1000,500,600]
plt.subplot(1,2,1)
plt.scatter(Games,users,marker="o",c=users,cmap="coolwarm",alpha=0.5)
plt.colorbar()
plt.title("Games")
plt.subplot(1,2,2)
plt.bar(["a","b"],[1,20],color=["red","blue"],edgecolor="Black")
plt.title("Label")
plt.subplot(2,2,4)
plt.pie(Games,users,colors=["r","g","b","y"],shadow=True,startangle=90)
plt.legend()
plt.show()"""

#Grid & figure size

"""plt.figure(figsize=(6,4))
plt.plot([1,2,3,4],[2,3,4,5])
plt.grid(True)
plt.show()"""

"""Cartoons = ["Ben 10","Power rangers","Enemy","Hell cat","Bet","Ace","Dora"]
Viewers = (110000,350000,4800000,2430000,650000000,30000000,820000000)
plt.figure (figsize=(8,10))
plt.scatter(Cartoons,Viewers,marker="o",c=Viewers,cmap="rainbow",edgecolor="black")
plt.colorbar()
plt.xlabel("cartoons")
plt.ylabel("viewers")
plt.xticks(rotation=30)
plt.grid(True)
plt.title("Cartoon_Datas")
plt.show()"""

#Axis Limits & save figure

"""Mobile = ["Nokia","Samsung","Lava","Oppo","Vivo","Redmi"]
Price = (10000,45000,5000,18000,20000,12000)
plt.figure(figsize=(8,7))
plt.grid(True)
plt.plot(Mobile,Price,color="y",linestyle=":",marker="o")
plt.xlim(1,6)
plt.ylim(0,50000)
plt.title("Mobile Chart")
plt.xlabel("Mobile")
plt.ylabel("price")
plt.savefig("chart.png")#Save the figure 
plt.show()"""

#Multiple subplot with figure

"""product = ["Colgate","Brush"]
Price = (25,36)
mrp = (20,30)
fig,ax=plt.subplot(2,1,1)
plt.figure(figsize=(6,7))
ax[0].plt.scatter(product,price,c=price,cmap="rainbow",marker="s",edgecolor="black")
ax[0].plt.colorbar()
ax[0].plt.set_title("Product VS price")
ax[0].plt.xlabel("product")
ax[0].plt.ylabel("price")
ax[0].plt.xticks(rotation=30)
ax[1].plt.plot(product,mrp,color="g",linestyle=":_",marker="S")
ax[1].plt.set_title("product VS mrp")
ax[1].plt.xlabel("product")
ax[1].plt.ylabel("mrp")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()"""

#Twin axis

"""Movies =["Avenger","Bet","Ace","Rangers","After Years"]
price = (150,200,180,200,150)
Seats = (300,100,150,122,43)
fig,ax1=plt.subplots()
plt.grid(True)
ax1.plot(Movies,price,linestyle=":",marker="o",color="y")
ax1.set_xlabel("Movies")
ax2=ax1.twinx()
ax2.plot(price,Seats,linestyle=":",marker="o",color="r")
ax2.set_ylabel("Price VS seats")
plt.yticks(rotation=30)
plt.tight_layout()
plt.title("Movies")
plt.show()"""
              

#Style sheet

"""plt.style.use('ggplot')
plt.style.use("seaborn-v0_8")
plt.style.use("fast")
plt.plot([1,2,3],[4,5,6])
plt.show()"""


#Multiple plot Types Together

"""Movies =["Avenger","Bet","Ace","Rangers","After Years"]
price = (150,200,180,200,150)
mycolor=["r","b","g","c","y"]


plt.plot(Movies,price,linestyle=":",marker="o")
plt.scatter(Movies,price,c=price,cmap="rainbow",marker="o",edgecolor="black")
plt.pie(price,labels=Movies,colors=mycolor,shadow=True)
plt.show()"""






























            




















