import matplotlib.pyplot as plt

for i in range(100):
    f = open('elec.csv','r')
    line = f.readline()
    member = line[:-1].split(',')
    line = f.readline()
    get = line[:-1].split(',')
    f.close()
    plt.figure(1, figsize=(10, 10))
    ex = [0.02]*len(member)
    plt.pie(get, explode = ex, labels=member, autopct='%1.1f%%',startangle=67)
    plt.title('Vote Percentage',fontsize = 30)
    plt.draw()
    plt.pause(10)
    plt.clf()