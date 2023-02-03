#!/home/ruili/anaconda3/bin/python3
import sys, os, shutil, glob
from pathlib import Path

apps = ["openssl", "cpython", "memcached", "redis", "httpd", "FFmpeg"]
#apps = ["FFmpeg"]
#apps = ["cpython"]
#apps = ["openssl", "cpython", "memcached", "redis", "httpd", "httpd1", "httpd2"]
#apps = ['httpd1']

root = str(Path.home()) + '/candidates/'

month_dic = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
             "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov":11, "Dec":12}

err_dic = {"func": 0, "perf":1, "safe":2, "incr":3, "corr":0, "na": 4, "nr": 4, "ir":4, "sec":2}

def get_blank_month():
    month = [0, 0, 0, 0] #func, perf, safe, incr
    return month

def get_blank_year():
    year = []
    for i in range(12):
        year.append([0, 0, 0, 0])
    return year

def trim_log(log_path):
    year_dict = {}

    year_dict["2021"] = get_blank_year()
    year_dict["2022"] = get_blank_year()

    error = ""
    with open(log_path, 'r') as f:
        for line in f:
            if "commit " in line:
                count = False
                if "] **new** commit " in line:
                    count = True
                    error = err_dic[line.split()[0].strip("[]").lower()]
            if line.startswith('Date: ') and count:
                year = (line.strip().split()[5])
                month = month_dic[line.strip().split()[2]]
                try:
                    year_dict[year][month-1][error]+=1
                except:
                    if error != 4:
                        print('Error!', year, month, error)
                #print("year:%s, month:%s, error:%s"%(year, month, error))
    errors = [0, 0, 0, 0]

    for year in year_dict.keys():
        for month in range(12):
            #for i in range(1, 4):
            #    year_dict[year][month][i] += year_dict[year][month][i - 1]
            print("%s%s" %(year, str(month+1).zfill(2)), end="  ")
            for i in range(4):
                errors[i] += year_dict[year][month][i]
                print("%s   " % (errors[i]), end = "")
            print()
    return year_dict
def read_api_list(app):
    #loc_dict = {}
    #os.chdir(root)
    log_path = app+'.adapted'
    #if os.path.exists(log_path):
    #    os.remove(log_path)
    #os.system('cat '+log_path+' > '+log_path+'1')
    #os.system('mv '+log_path+'1 '+log_path)
    return trim_log(log_path)
    #return loc_dict
    
all_app_year_dicts = {}
for app in apps:
    #all_commit, year_valid_commit = read_api_list(app)
    #print(app, all_commit, year_valid_commit)

    all_app_year_dicts[app] = read_api_list(app)
    print('******************************', app, '******************************' )

errors = [0, 0, 0, 0]

year_dict = {}
year_dict["2021"] = get_blank_year()
year_dict["2022"] = get_blank_year()

for year in year_dict.keys():
    for month in range(12):
        #for i in range(1, 4):
        #    year_dict[year][month][i] += year_dict[year][month][i - 1]
        print("%s%s" %(year, str(month+1).zfill(2)), end="  ")
        for i in range(4):
            for app in apps:
                errors[i] += all_app_year_dicts[app][year][month][i]
            print("%s   " % (errors[i]), end = "")
        print()

    #print(year_dict)
