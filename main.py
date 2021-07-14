#from nqs import write, run
from egg import sleep, eggConsole, install, Repo

f="example2"
#eggConsole()
#run(f)
#write(f)

install("matplotlib")

covid=Repo("CovidPlot")
cp=covid.pull("covidplot","CovidData")
#pull("CovidPlot")
covidata=cp.CovidData
c=covidata()
c.plot