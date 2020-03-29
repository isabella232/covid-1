```
##Single curve
python find_curve.py covid-cases-by-source.csv india.csv india

##Mltiple Curves
#Generate the data
cd data
python ../split.py covid_confirmed_usafacts.csv

#Generate the plots
ls data/*|cut -d "/" -f 2|sort -n|cut -d "." -f 1|tail -n 20|xargs -I % python find_curve.py covid-cases-by-source.csv data/%.csv plot/%

#Update the README
cd plot
ls |sort -n -r |grep png|xargs -I % echo '![image](plot/%)' >> ../README.md 
```
![image](plot/8115_new_york_city_NY.png)
![image](plot/1385_westchester_county_NY.png)
![image](plot/1234_nassau_county_NY.png)
![image](plot/934_king_county_WA.png)
![image](plot/662_suffolk_county_NY.png)
![image](plot/548_cook_county_IL.png)
![image](plot/447_snohomish_county_WA.png)
![image](plot/418_orleans_parish_LA.png)
![image](plot/363_bergen_county_NJ.png)
![image](plot/351_los_angeles_county_CA.png)
![image](plot/349_wayne_county_MI.png)
![image](plot/263_santa_clara_county_CA.png)
![image](plot/262_rockland_county_NY.png)
![image](plot/229_oakland_county_MI.png)
![image](plot/177_middlesex_county_MA.png)
![image](plot/169_miami-dade_county_FL.png)
![image](plot/166_jefferson_parish_LA.png)
![image](plot/164_broward_county_FL.png)
![image](plot/163_albany_county_NY.png)
![image](plot/148_san_diego_county_CA.png)
