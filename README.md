cd data
python ../split.py covid_confirmed_usafacts.csv
ls data/*|cut -d "/" -f 2|sort -n|cut -d "." -f 1|tail -n 20|xargs -I % python find_curve.py covid-cases-by-source.csv data/%.csv plot/%

[image](plot/1234_nassau_county_NY.png)
