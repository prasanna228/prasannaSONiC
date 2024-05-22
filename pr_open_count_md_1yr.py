#!/usr/sbin/env python

#From https://towardsdatascience.com/github-user-insights-using-github-api-data-collection-and-analysis-5b7dca1ab214


import os
import json
import sys
import requests
from requests.auth import HTTPBasicAuth
from collections import defaultdict
import variables
from datetime import datetime as dt
from datetime import timedelta
import dateutil
import glob
from collections import defaultdict

dell_pulls_per_user_per_repo = defaultdict(dict)
bcm_pulls_per_user_per_repo = defaultdict(dict)
mlnx_pulls_per_user_per_repo = defaultdict(dict)

credentials = json.loads(open('credentials.json').read())
authentication = HTTPBasicAuth(credentials['username'], credentials['password'])


def add_to_dell_pulls(commit_user,repo,pulls):
    for user in variables.dell_users:
        if user == commit_user:
            dell_pulls_per_user_per_repo[user][repo] += pulls

def add_to_bcm_pulls (commit_user,repo,pulls):
    for user in variables.bcm_users:
        if user == commit_user:
            bcm_pulls_per_user_per_repo[user][repo] += pulls

def add_to_mlnx_pulls (commit_user,repo,pulls):
    for user in variables.mlnx_users:
        if user == commit_user:
            mlnx_pulls_per_user_per_repo[user][repo] += pulls

for user in variables.dell_users:
    for repo in variables.repos:
        dell_pulls_per_user_per_repo[user][repo] = 0

for user in variables.bcm_users:
    for repo in variables.repos:
        bcm_pulls_per_user_per_repo[user][repo] = 0

for user in variables.mlnx_users:
    for repo in variables.repos:
        mlnx_pulls_per_user_per_repo[user][repo] = 0

repo_count = len (variables.repos)
#print ("KVSK1: repo_count={}".format(repo_count))
all_users=[[] for i in range(repo_count)]
repowise_pr_age_dict = {}
repo_index = 0
for repo in variables.repos:
    #if repo != "sonic-swss-common":
    #    continue
    url_to_get =  'https://api.github.com/repos/Azure/'+repo+'/pulls?state=all'
#    url_to_get =  'https://api.github.com/repos/pyuvarajan/Test-Local/pulls'
    print ("KVSK:URL={}".format (url_to_get))
    users_data = []
    contributors = []
    repowise_pr_age_dict[repo] = {}
    repowise_pr_age_dict[repo]['7daysold'] = {}
    repowise_pr_age_dict[repo]['14daysold'] = {}
    repowise_pr_age_dict[repo]['30daysold'] = {}
    repowise_pr_age_dict[repo]['90daysold'] = {}
    repowise_pr_age_dict[repo]['MoreThan90daysold'] = {}
    repowise_pr_age_dict[repo]['MoreThan1yrold'] = {}
    repowise_pr_age_dict[repo]['7daysold']['count'] = 0
    repowise_pr_age_dict[repo]['7daysold']['pr_list'] = []
    repowise_pr_age_dict[repo]['14daysold']['count'] = 0
    repowise_pr_age_dict[repo]['14daysold']['pr_list'] = []
    repowise_pr_age_dict[repo]['30daysold']['count'] = 0
    repowise_pr_age_dict[repo]['30daysold']['pr_list'] = []
    repowise_pr_age_dict[repo]['90daysold']['count'] = 0
    repowise_pr_age_dict[repo]['90daysold']['pr_list'] = []
    repowise_pr_age_dict[repo]['MoreThan90daysold']['count'] = 0
    repowise_pr_age_dict[repo]['MoreThan90daysold']['pr_list'] = []
    repowise_pr_age_dict[repo]['MoreThan1yrold']['count'] = 0
    repowise_pr_age_dict[repo]['MoreThan1yrold']['pr_list'] = []
    
    total_pulls=0
    page_no = 1
    while (True):
        response = requests.get(url_to_get, auth = authentication)
        response = response.json()
        pulls_fetched = len(response)
        #print("pulls fetched: {}".format(pulls_fetched))
        if (pulls_fetched == 30):
            for i in range (0, 30):
                if (response[i]['state'] == "closed"):
                    continue
                datetimestr = response[i]['created_at']
                date_str = datetimestr.split('T')[0]
                pr_date = dt.strptime(date_str, '%Y-%m-%d') 
                #pr_date = dateutil.parser.parse('date')
                #print ("PR Date = {} state = {}".format( date_str, response[i]['state']))
                time_between_pr = dt.now() - pr_date
                if  time_between_pr.days<7:
                    print ("The pr= {} is maximum 7 days old".format(response[i]['number']))
                    repowise_pr_age_dict[repo]['7daysold']['count'] += 1
                    repowise_pr_age_dict[repo]['7daysold']['pr_list'].append(response[i]['number'])
                elif  time_between_pr.days<14:
                    repowise_pr_age_dict[repo]['14daysold']['count'] += 1
                    repowise_pr_age_dict[repo]['14daysold']['pr_list'].append(response[i]['number'])
                    #repowise_pr_age_dict[repo]['14daysold'].count += 1
                    print ("The pr= {} is maximum 14 days old".format(response[i]['number']))
                elif  time_between_pr.days<30:
                    repowise_pr_age_dict[repo]['30daysold']['count'] += 1
                    repowise_pr_age_dict[repo]['30daysold']['pr_list'].append(response[i]['number'])
                    #repowise_pr_age_dict[repo]['30daysold'].count += 1
                    print ("The pr= {} is maximum 30 days old".format(response[i]['number']))
                elif  time_between_pr.days<90:
                    repowise_pr_age_dict[repo]['90daysold']['count'] += 1
                    repowise_pr_age_dict[repo]['90daysold']['pr_list'].append(response[i]['number'])
                    #repowise_pr_age_dict[repo]['90daysold'].count += 1
                    print ("The pr= {} is maximum 90 days old".format(response[i]['number']))
                elif  time_between_pr.days<365:
                    repowise_pr_age_dict[repo]['MoreThan90daysold']['count'] += 1
                    repowise_pr_age_dict[repo]['MoreThan90daysold']['pr_list'].append(response[i]['number'])
                    #repowise_pr_age_dict[repo]['MoreThan90daysold'].count += 1
                    print ("The pr= {} is maximum 1 year old".format(response[i]['number']))
                else:
                    repowise_pr_age_dict[repo]['MoreThan1yrold']['count'] += 1
                    repowise_pr_age_dict[repo]['MoreThan1yrold']['pr_list'].append(response[i]['number'])
                    #repowise_pr_age_dict[repo]['MoreThan1yrold'].count += 1
                    print ("The pr= {}  is open beyond 1 year".format(response[i]['number']))
            page_no = page_no + 1
            #url_to_get = url_to_get.split('?')[0]
            url_to_get = url_to_get + '&page=' + str(page_no)
#            print ("KVSK:url_to_get={}".format(url_to_get))
        else:
            for i in range (0, pulls_fetched):
                datetime = response[i]['created_at']
            break
    
    repo_index = repo_index + 1


#print (repowise_pr_age_dict)
for repo in variables.repos:
    print ("Repo = {}".format(repo))
    if  repowise_pr_age_dict[repo]['7daysold']['count'] != 0:
        print ("7DaysOldCount = {} and the PRs are {}".format(repowise_pr_age_dict[repo]['7daysold']['count'], repowise_pr_age_dict[repo]['7daysold']['pr_list']))
    else:
        print ("7DaysOldCount = {}".format(0))
    if  repowise_pr_age_dict[repo]['90daysold']['count'] != 0:
        print ("90DaysOldCount = {} and the PRs are {}".format(repowise_pr_age_dict[repo]['90daysold']['count'], repowise_pr_age_dict[repo]['90daysold']['pr_list']))
    else:
        print ("90DaysOldCount = {}".format(0))

pr_list_pr_num_and_link = ""

#open a file with access mode 'a'
#file_object = open('pr_open_count.md', 'w+')
#str_heading = "| Repo | 7DaysOldPRs | 14DaysOldPRs | 30DaysOldPRs | 90DaysOldPRs | MoreThan90DaysOldPR |"
#file_object.write(str_heading)
#file_object.write("\n")
#str_underline = "|------|-------------|--------------|--------------|--------------|---------------------|"
#file_object.write(str_underline)
#file_object.write("\n")
html_dict_1 = {}
list_for_search_and_replace = []
for repo in variables.repos:
    str1 = "|"+repo
    html_dict_1[repo] = repo
    daysstr7 = "| "
    if  repowise_pr_age_dict[repo]['7daysold']['count'] != 0:
        str2 = "Count = "+ str(repowise_pr_age_dict[repo]['7daysold']['count'])+" ( " 
        temp_dict = {}
        var_name1 = repo+'_7daysold'
        var_value1 = "Count = "+ str(repowise_pr_age_dict[repo]['7daysold']['count'])+" ("
        for pr in repowise_pr_age_dict[repo]['7daysold']['pr_list']:
             var_value1 += "["+str(pr)+"]("+"https://github.com/Azure/"+repo+"/pull/"+str(pr)+"), "
#            list1 = {}
        #    temp_dict[var_name]  = var_value
#            list1(temp_dict)
        # Remove the extra comma and a blank space from the last
        var_value1 = var_value1[:-2]
        var_value1 += ")"
        str2 += pr_list_pr_num_and_link
        daysstr7 += str2+" ABCD )"
        #html_dict_1['7DaysOldPRs'] = daysstr7
        temp_dict['var_name'] = var_name1
        temp_dict['var_val'] = var_value1
        list_for_search_and_replace.append(temp_dict)
#        var_value1_md = "Count = "+ str(repowise_pr_age_dict[repo]['7daysold']['count'])+" ("
#        temp_dict_md = {}
#        var_name1_md = repo+'_7daysold'
#        var_value1_md += pr_list_pr_num_and_link
#        daysstr7 += var_value1_md+")"
#        temp_dict_md['var_name_md'] = var_name1_md
#        temp_dict_md['var_val_md'] = var_value1_md
#        list_for_search_and_replace.append(temp_dict_md)
    else:
        str2 = "Count = 0"
        daysstr7 += str2
        temp_dict = {}
        var_name1 = repo+'_7daysold'
        var_value1 = "Count = 0"
        temp_dict['var_name'] = var_name1
        temp_dict['var_val'] = var_value1
        list_for_search_and_replace.append(temp_dict)
        html_dict_1['7DaysOldPRs'] = daysstr7
    daysstr14 = "| "
    if  repowise_pr_age_dict[repo]['14daysold']['count'] != 0:
        str2 = "Count = "+ str(repowise_pr_age_dict[repo]['14daysold']['count'])+" ("
        for pr in repowise_pr_age_dict[repo]['14daysold']['pr_list']:
            pr_list_pr_num_and_link = "["+str(pr)+"]("+"https://github.com/Azure/"+repo+"/pull/"+str(pr)+"), "
            str2 += pr_list_pr_num_and_link
        daysstr14 += str2+")"
        temp_dict = {}
        var_name1 = repo+'_14daysold'
        var_value1 = "Count = "+ str(repowise_pr_age_dict[repo]['14daysold']['count'])+" ("
        for pr in repowise_pr_age_dict[repo]['14daysold']['pr_list']:
             var_value1 += "["+str(pr)+"]("+"https://github.com/Azure/"+repo+"/pull/"+str(pr)+"), "
        var_value1 = var_value1[:-2]
        var_value1 += ")"
        temp_dict['var_name'] = var_name1
        temp_dict['var_val'] = var_value1
        list_for_search_and_replace.append(temp_dict)
        html_dict_1['14DaysOldPRs'] = daysstr14
    else:
        str2 = "Count = 0"
        daysstr14 += str2
        temp_dict = {}
        var_name1 = repo+'_14daysold'
        var_value1 = "Count = 0"
        temp_dict['var_name'] = var_name1
        temp_dict['var_val'] = var_value1
        list_for_search_and_replace.append(temp_dict)
        html_dict_1['14DaysOldPRs'] = daysstr14
    daysstr30 = "| "
    if  repowise_pr_age_dict[repo]['30daysold']['count'] != 0:
        str2 = "Count = "+ str(repowise_pr_age_dict[repo]['30daysold']['count'])+" ("
        for pr in repowise_pr_age_dict[repo]['30daysold']['pr_list']:
            pr_list_pr_num_and_link = "["+str(pr)+"]("+"https://github.com/Azure/"+repo+"/pull/"+str(pr)+"), "
            str2 += pr_list_pr_num_and_link
        daysstr30 += str2+")"
        temp_dict = {}
        var_name1 = repo+'_30daysold'
        var_value1 = "Count = "+ str(repowise_pr_age_dict[repo]['30daysold']['count'])+" ("
        for pr in repowise_pr_age_dict[repo]['30daysold']['pr_list']:
             var_value1 += "["+str(pr)+"]("+"https://github.com/Azure/"+repo+"/pull/"+str(pr)+"), "
        var_value1 = var_value1[:-2]
        var_value1 += ")"
        temp_dict['var_name'] = var_name1
        temp_dict['var_val'] = var_value1
        list_for_search_and_replace.append(temp_dict)
        html_dict_1['30DaysOldPRs'] = daysstr30
    else:
        str2 = "Count = 0"
        daysstr30 += str2
        temp_dict = {}
        var_name1 = repo+'_30daysold'
        var_value1 = "Count = 0" 
        temp_dict['var_name'] = var_name1
        temp_dict['var_val'] = var_value1
        list_for_search_and_replace.append(temp_dict)
        html_dict_1['30DaysOldPRs'] = daysstr30
    daysstr90 = "| "
    if  repowise_pr_age_dict[repo]['90daysold']['count'] != 0:
        str2 = "Count = "+ str(repowise_pr_age_dict[repo]['90daysold']['count'])+" ("
        for pr in repowise_pr_age_dict[repo]['90daysold']['pr_list']:
            pr_list_pr_num_and_link = "["+str(pr)+"]("+"https://github.com/Azure/"+repo+"/pull/"+str(pr)+"), "
            str2 += pr_list_pr_num_and_link
        daysstr90 += str2+")"
        temp_dict = {}
        var_name1 = repo+'_90daysold'
        var_value1 = "Count = "+ str(repowise_pr_age_dict[repo]['90daysold']['count'])+" ("
        for pr in repowise_pr_age_dict[repo]['90daysold']['pr_list']:
             var_value1 += "["+str(pr)+"]("+"https://github.com/Azure/"+repo+"/pull/"+str(pr)+"), "
        var_value1 = var_value1[:-2]
        var_value1 += ")"
        temp_dict['var_name'] = var_name1
        temp_dict['var_val'] = var_value1
        list_for_search_and_replace.append(temp_dict)    
        html_dict_1['90DaysOldPRs'] = daysstr90
    else:
        str2 = "Count = 0"
        daysstr90 += str2
        temp_dict = {}
        var_name1 = repo+'_90daysold'
        var_value1 = "Count = 0"
        temp_dict['var_name'] = var_name1
        temp_dict['var_val'] = var_value1
        list_for_search_and_replace.append(temp_dict)
        html_dict_1['90DaysOldPRs'] = daysstr90
    MoreThan90Str = "| "
    if  repowise_pr_age_dict[repo]['MoreThan90daysold']['count'] != 0:
        str2 = "Count = "+ str(repowise_pr_age_dict[repo]['MoreThan90daysold']['count'])+" ("
        for pr in repowise_pr_age_dict[repo]['MoreThan90daysold']['pr_list']:
            pr_list_pr_num_and_link = "["+str(pr)+"]("+"https://github.com/Azure/"+repo+"/pull/"+str(pr)+"), "
            str2 += pr_list_pr_num_and_link
        MoreThan90Str += str2+")"+"|"
        temp_dict = {}
        var_name1 = repo+'_MoreThan90daysold'
        var_value1 = "Count = "+ str(repowise_pr_age_dict[repo]['MoreThan90daysold']['count'])+" ("
        for pr in repowise_pr_age_dict[repo]['MoreThan90daysold']['pr_list']:
             var_value1 += "["+str(pr)+"]("+"https://github.com/Azure/"+repo+"/pull/"+str(pr)+"), "
        var_value1 = var_value1[:-2]
        var_value1 += ")"
        temp_dict['var_name'] = var_name1
        temp_dict['var_val'] = var_value1
        list_for_search_and_replace.append(temp_dict) 
        html_dict_1['MoreThan90DaysOldPR'] = MoreThan90Str
    else:
        str2 = "Count = 0"
        MoreThan90Str += str2+"|"
        temp_dict = {}
        var_name1 = repo+'_MoreThan90daysold'
        var_value1 = "Count = 0"
        temp_dict['var_name'] = var_name1
        temp_dict['var_val'] = var_value1
        list_for_search_and_replace.append(temp_dict)
        html_dict_1['MoreThan90DaysOldPR'] = MoreThan90Str
    daysstr1yr = "| "
    if  repowise_pr_age_dict[repo]['MoreThan1yrold']['count'] != 0:
        str2 = "Count = "+ str(repowise_pr_age_dict[repo]['MoreThan1yrold']['count'])+" ("
        for pr in repowise_pr_age_dict[repo]['MoreThan1yrold']['pr_list']:
            pr_list_pr_num_and_link = "["+str(pr)+"]("+"https://github.com/Azure/"+repo+"/pull/"+str(pr)+"), "
            str2 += pr_list_pr_num_and_link
        daysstr1yr += str2+")"
        temp_dict = {}
        var_name1 = repo+'_MoreThan1yrold'
        var_value1 = "Count = "+ str(repowise_pr_age_dict[repo]['MoreThan1yrold']['count'])+" ("
        for pr in repowise_pr_age_dict[repo]['MoreThan1yrold']['pr_list']:
             var_value1 += "["+str(pr)+"]("+"https://github.com/Azure/"+repo+"/pull/"+str(pr)+"), "
        var_value1 = var_value1[:-2]
        var_value1 += ")"
        temp_dict['var_name'] = var_name1
        temp_dict['var_val'] = var_value1
        list_for_search_and_replace.append(temp_dict)
        html_dict_1['MoreThan1yroldPRs'] = daysstr1yr
    else:
        str2 = "Count = 0"
        daysstr1yr += str2
        temp_dict = {}
        var_name1 = repo+'_MoreThan1yrold'
        var_value1 = "Count = 0"
        temp_dict['var_name'] = var_name1
        temp_dict['var_val'] = var_value1
        list_for_search_and_replace.append(temp_dict)
        html_dict_1['MoreThan1yroldPRs'] = daysstr1yr    
    final_str = str1+daysstr7+daysstr14+daysstr30+daysstr90+MoreThan90Str+daysstr1yr
#    file_object.write(final_str)
#    file_object.write("\n")

# Append 'hello' at the end of file
# Close the file
#file_object.close()

for element in list_for_search_and_replace:
   print ("Var_name = {} and var_value = {}".format (element['var_name'], element['var_val']))

fin = open("pr_open_count_template_md.md", "rt")
data = fin.read()
fin.close()
fout = open("pr_open_count.md", "wt")
for element in list_for_search_and_replace:
   print ("Var_name = {} and var_value = {}".format (element['var_name'], element['var_val']))
   #replace all occurrences of the required string
   data = data.replace(element['var_name'], element['var_val'])
fout.write(data)
#close input and output files
fout.close()




#file_ = open('pr_open_count.html', 'w')

#file_.write(html)


#with open('pr_open_count.html', 'w') as report:
#    report.write('<html>')
#    report.write('<body>')
#
#for key,value in html_dict_1.iteritems():
#    report.write('<div>{}</div><div>{}</div>\n'.format(key, value))


#LIST OF DICTS
# Entry1 DICT: dict1['syncd_7daysold'] = string1
# Entry2 DICT: dict1['syncd_14daysold'] = string2
# ....
# Entryn DICT: dict1['reponame_7daysold'] = stringn1

#for  in  list:
#   dict1key  will be syncd_7daysold 
#   dict1key_value  will be string1 
#   open html file
#   search for dict1key  in file and replace it with string1; may be a regex

#for element in list_for_search_and_replace:
#   print ("Var_name = {} and var_value = {}".format (element['var_name'], element['var_val']))


#html = """<html><table border="1"><tr><th>Repo</th><th>7DaysOldPRs</th><th>14DaysOldPRs</th><th>30DaysOldPRs</th><th>90DaysOldPRs</th><th>MoreThan90DaysOldPR</th></tr>"""

#<tr><th>Repo</th><th>7DaysOldPRs</th><th>14DaysOldPRs</th><th>30DaysOldPRs</th><th>90DaysOldPRs</th><th>MoreTahn90DaysOldPRs</th></tr>"""

#fin = open("pr_open_count_template.html", "rt")
#read file contents to string
#data = fin.read()
#close the input file
#fin.close()
#open the input file in write mode
#fout = open("pr_open_count.html", "wt")
#for element in list_for_search_and_replace:
#   print ("Var_name = {} and var_value = {}".format (element['var_name'], element['var_val']))
   #replace all occurrences of the required string
#   data = data.replace(element['var_name'], element['var_val'])
#fout.write(data)
#close input and output files
#fout.close()

#for rep in html_dict_1:
#    html += "<tr><td>{}</td>".format(rep)
#for syncd_7daysold in pr_open_count.html:
#    v.replace_with('var_value')

#    for syncd_7daysold == temp_dict
#    for daysstr in "7DaysOldPRs","14DaysOldPRs","30DaysOldPRs","90DaysOldPRs","MoreThan90daysold":
#        html += "<td>{}</td>".format('<br>'.join(f for f in html_dict_1[rep] if ".{}.".format(daysstr) in f))
#        html += "<td>{}</td>".format(html_dict_1[daysstr])
#        html += "<td>{}</td>".format(html_dict_1[daysstr7])
#        html += "<td>{}</td>".format(html_dict_1[daysstr14])
#        html += "<td>{}</td>".format(html_dict_1[daysstr30])
#        html += "<td>{}</td>".format(html_dict_1[daysstr90])
#        html += "<td>{}</td>".format(html_dict_1[MoreThan90Str])
#html += "</tr>"
#html += "</table></html>"

#file_ = open('pr_open_count.html', 'w')

#file_.write(html)

#file_.close()
