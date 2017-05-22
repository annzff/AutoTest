import json
import MySQLdb
from varclass import VarClass

def myconn1():
    conn1 = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='moyan', db='ocr_2', charset='utf8')
    cursor1 = conn1.cursor()
    sql2='select vcard from weixin_card_yj where id="2249"'
    cursor1.execute(sql2)
    results1=cursor1.fetchall()
    #print results
    data1 = json.loads(results1[0][0])
    #print data
    return data1

def myconn2():
    conn2 = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='moyan', db='ocr_2', charset='utf8')
    cursor2 = conn2.cursor()
    sql2='select vcard from weixin_card_yj where id="2249"'
    cursor2.execute(sql2)
    results2=cursor2.fetchall()
    #print results
    data2 = json.loads(results2[0][0])
    #print data
    return data2


def check_key(jdict,key):

    if isinstance(jdict, list):
        for element in jdict:
            if key == element:
                c.obj_value = jdict[element]
                return True
        return False
    elif isinstance(jdict, dict):
        for x in jdict.keys():
            if x == key:
                c.obj_value = jdict[x]
                return True
        return False

def check_layer(jdict,key):
    flag = False

    for layer in jdict:
        if isinstance(jdict, list):
            flag = check_key(layer, key)
            if flag == True:
                return flag
            else:
                continue
        if len(jdict) == 1 and len(layer) == 1:
            continue
        else:
            flag = check_key(jdict[layer], key)
        if flag == True:
            return flag
        else:
            if len(jdict) == 1 and len(layer) == 1:
                continue
            flag = check_layer(jdict[layer], key)
            if flag == True:
                return flag
    return False


#
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except(TypeError,ValueError):
        pass

    return False

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def check_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00'<=ch<=u'\u9fff':
            return True
    return False



def autoTest():

    res1 = myconn1()
    res2 = myconn2()

    if(check_layer(res2,'name')):
        str_name1=c.obj_value[0]['value']
        c.sum_name = c.sum_name + 1

        if(check_layer(res1,'name')):
            str_name2=c.obj_value[0]['value']

            if(check_chinese(str_name2)):
                c.sum_chinese=c.sum_chinese+len(str_name2)

            if str_name1 in str_name2:
                c.correct_name=c.correct_name+1
                c.correct_chinese = c.correct_chinese + len(str_name1)
            if(str_name1!=str_name2):
                print 'name error'

        else:
            #write error
            print 'name error'


    #
    #company_name
    if(check_layer(res2,'company_name')):
        str_company_name1=c.obj_value[0]['value']
        c.sum_company_name = c.sum_company_name + 1

        if(check_layer(res1,'company_name')):
            str_company_name2=c.obj_value[0]['value']

            if(check_chinese(str_company_name2)):
                c.sum_chinese=c.sum_chinese+len(str_company_name2)

            if str_company_name1 in str_company_name2:
                c.correct_company_name=c.correct_company_name+1
                c.correct_chinese = c.correct_chinese + len(str_company_name1)

            if(str_company_name1!=str_company_name2):
                print 'name error'

        else:
            # write error
            print 'company_name error'



    #job
    if (check_layer(res2, 'job')):
        str_job1=c.obj_value[0]['value']
        c.sum_job = c.sum_job + 1

        if (check_layer(res1, 'job')):
            str_job2=c.obj_value[0]['value']

            if(check_chinese(str_job2)):
                c.sum_chinese=c.sum_chinese+len(str_job2)

            if str_job1 in str_job2:
                c.correct_job=c.correct_job+1
                c.correct_chinese = c.correct_chinese + len(str_job1)

            if(str_job1!=str_job2):
                print 'job error'
        else:
            # write error
            print 'job error'



    #mobile
    if(check_layer(res2,'mobile')):
        str_mobile1=c.obj_value[0]['value']
        c.sum_mobile = c.sum_mobile + 1

        if(check_layer(res1,'mobile')):
            str_mobile2=c.obj_value[0]['value']

            if(is_number(str_mobile2)):
                c.sum_notchinese=c.sum_notchinese+len(str_mobile2)

            if str_mobile1 in str_mobile2:
                c.correct_mobile=c.correct_mobile+1
                c.correct_notchinese = c.correct_notchinese + len(str_mobile1)

            if(str_mobile1!=str_mobile2):
                print 'mobile error'

        else:
         # write error
            print 'mobile error'




    #telephone
    if(check_layer(res2,'telephone')):
        str_telephone1=c.obj_value[0]['value']
        c.sum_telephone = c.sum_telephone + 1

        if(check_layer(res1,'telephone')):
            str_telephone2=c.obj_value[0]['value']

            if(is_number(str_telephone2)):
                c.sum_notchinese=c.sum_notchinese+len(str_telephone2)

            if str_telephone1 in str_telephone2:
                c.correct_telephone=c.correct_telephone+1
                c.correct_notchinese = c.correct_notchinese + len(str_telephone1)

            if (str_telephone1!=str_telephone2):
                print 'telephone error'

        else:
            # write error
            print 'telephone error'


    #address
    if(check_layer(res2,'address')):
        str_address1=c.obj_value[0]['value']
        c.sum_address = c.sum_address + 1

        if(check_layer(res1,'address')):
            str_address2=c.obj_value[0]['value']

            if(check_chinese(str_address2)):
                c.sum_chinese=c.sum_chinese+len(str_address2)

            if str_address1 in str_address2:
                c.correct_address=c.correct_address+1
                c.correct_chinese = c.correct_chinese + len(str_address1)

            if(str_address1!=str_address2):
                print 'address error'

        else:
            #write error
            print 'address error'
def comp_lanmu():

    c.sum_lanmu=c.sum_name+c.sum_company_name+c.sum_telephone+c.sum_mobile+c.sum_address+c.sum_job
    c.correct_lanmu=c.correct_name+c.sum_company_name+c.correct_telephone+c.correct_mobile+c.correct_address+c.correct_job

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def draw_bar(labels,quants):

    width=0.4
    #ind=np.linspace(0,1,9)
    ind=[0,1,2,3,4,5,6,7,8]

    fig=plt.figure(1)
    ax=fig.add_subplot(111)

    ax.bar(ind,quants,width,color='green')

    ax.set_xticks(ind)
    ax.set_xticklabels(labels)

    ax.set_xlabel('lanmu',fontsize=16)
    ax.set_ylabel('accuracy',fontsize=16)

    ax.set_title('recognition accuracy',fontsize=18,bbox={'facecolor':'2','pad':10})

    plt.grid(True)
    plt.show()
    plt.savefig('bar.jpg')
    plt.close()

def draw_bar1(labels,quants1,quants2):

    a=quants1
    b=quants2

    fig = plt.figure(1)
    ax=fig.add_subplot(111)
    x=np.arange(6)

    total_width,n=0.8,2
    width1=total_width/n
    x=x-(total_width-width1)/2

    ind = [0, 1, 2, 3, 4, 5]
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)

    ax.set_xlabel('lanmu',fontsize=16)
    ax.set_ylabel('sum',fontsize=16)

    ax.set_title('lanmu sum',fontsize=18,bbox={'facecolor':'2','pad':10})

    plt.bar(x,a,width=width1,label='sum_lanmu')
    plt.bar(x+width1,b,width=width1,label='sum_correct_lanmu')

    plt.grid(True)
    plt.legend(loc='upper right')
    plt.show()
    plt.savefig('bar1.jpg')
    plt.close()



if __name__ == "__main__":

    c=VarClass()
    autoTest()
    comp_lanmu()


    #print
    print ''
    print '************************************************'
    print "sum_name:",c.sum_name
    print "correct_name:", c.correct_name
    print ''
    print "sum_company_name:", c.sum_company_name
    print "correct_company_name:", c.correct_company_name
    print ''
    print "sum_job:", c.sum_job
    print "correct_job:", c.correct_job
    print ''
    print "sum_mobile:", c.sum_mobile
    print "correct_mobile:", c.correct_mobile
    print ''
    print "sum_telephone:", c.sum_telephone
    print "correct_telephone:", c.correct_telephone
    print ''
    print "sum_address:", c.sum_address
    print "correct_address:", c.correct_address
    print ''
    print "sum_lanmu:",c.sum_lanmu
    print "correct_lanmu:", c.correct_lanmu
    print ''
    print "sum_chinese", c.sum_chinese
    print "correct_chinese", c.correct_chinese
    print ''
    print "sum_notchiness:", c.sum_notchinese
    print "correct_notchiness:", c.correct_notchinese
    print '************************************************'
    print ''
    print '------------------------------------------------'


    #correct rate
    if(c.sum_name!=0):
        c.rate_correct_name=c.correct_name/c.sum_name
        print "rate_correct_name:",c.rate_correct_name

    if(c.sum_company_name!=0):
        c.rate_correct_company_name=c.correct_company_name/c.sum_company_name
        print "rate_correct_company_name:",c.rate_correct_company_name

    if(c.sum_job!=0):
        c.rate_correct_job=c.correct_job/c.sum_job
        print "rate_correct_job:",c.rate_correct_job

    if(c.sum_mobile!=0):
        c.rate_correct_mobile=c.correct_mobile/c.sum_mobile
        print "rate_correct_mobile:",c.rate_correct_mobile

    if(c.sum_telephone!=0):
        c.rate_correct_telephone=c.correct_telephone/c.sum_telephone
        print "rate_correct_telephone:",c.rate_correct_telephone

    if(c.sum_address!=0):
        c.rate_correct_address=c.correct_address/c.sum_address
        print "rate_correct_address:",c.rate_correct_address

    if(c.sum_lanmu!=0):
        c.rate_lanmu=c.correct_lanmu/c.sum_lanmu
        print "rate_lanmu:", c.rate_correct_address
    print '-------------------------------------------------'


    #store error



    #plot
    labels=['name','company_name ','job','mobile','telephone','address','lanmu','chinese','notchinese']
    quants=[c.rate_correct_name,c.rate_correct_company_name,c.rate_correct_job,c.rate_correct_mobile,
            c.rate_correct_telephone,c.rate_correct_address,c.rate_lanmu,c.rate_chinese,c.rate_notchinese]
    draw_bar(labels,quants)


    labels1=['name','company_name ','job','mobile','telephone','address']
    quants1=[c.sum_name,c.sum_company_name,c.sum_job,c.sum_mobile,c.sum_telephone,c.sum_address]
    quants2=[c.correct_name,c.correct_company_name,c.correct_job,c.correct_mobile,c.correct_telephone,c.correct_address]

    draw_bar1(labels1,quants1,quants2)


    #error_lanmu = {'1':('shouji','dianhua'),'2':'dizhi','3':('danwei','xinming')}
    #print error_lanmu['3']