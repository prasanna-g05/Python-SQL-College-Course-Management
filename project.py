import mysql.connector as myc
from tabulate import tabulate
con=myc.connect(host="localhost",user='root',passwd='pg262004',database='project')
cur=con.cursor()
'''
cur.execute("create table streams(stream char(20), sub_stream char(20) primary key)")
cur.execute("insert into streams(stream,sub_stream) values(%s,%s)", ('science', 'pcm'))
cur.execute("insert into streams(stream,sub_stream) values(%s,%s)", ('science', 'pcb'))
cur.execute("insert into streams(stream,sub_stream) values(%s,%s)", ('arts', 'arts'))
cur.execute("insert into streams(stream,sub_stream) values(%s,%s)", ('commerce', 'commerce'))
con.commit()

cur.execute("create table substream(sub_stream char(20), foreign key(sub_stream) references streams(sub_stream),courses char(100),top_3_colleges char(200),\
average_fees int(8))")
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcm', 'aeronautical engineering','DSCE Bangalore,Kumaraguru\
college of Technology,Sathyabama University','360000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcm','information technology','COEP Pune,SRM University \
Chennai,RVCE Bangalore','270000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcm','chemical engineering','IIT Bombay,VIT Vellore,IIT Madras\
','750000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcm','electrical engineering','LPU University,\
DTU Delhi,MSRIT Bangalore','570000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcm','power engineering','SRM University,DSCE Bangalore,\
VIT Vellore','659000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcm','software engineering','Bennett University,IIT Bombay,\
MIT Manipal','980000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcm','artificial engineering','Chandigad University,IIT Hyderabad,\
Sastra University','650000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcm','nuclear engineering','Sastra Univesity,Jadarpur University,\
Amity University','780000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcm','robotics','IIT Hyderabad,IIT kanpur,MIT','875000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcm','mechanical engineering','IIT Bombay,MIT,COEP Pune','\
850000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcm','B.Sc in Physics','IIT Hyderabad,IIS Bangalore,Satyabama\
 University','894000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcm','B.Sc in Chemistry','SRM University,IIS Bangalore,IIT\
 Bombay','750000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcm','B.Sc in Mathematics','VIT Vellore,IIT Madras,SRM \
University','680000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcm','B.Sc in Astrophysics','Fergussion College,IIA Banalore\
,IIT Madras','980000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcm','CS Programmer','IIT Madras,IIT Bombay,IIT Kanpur\
','890000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcb','MBBS','CMC Vellore,KMC Mangalore,AIIMS','670000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcb','BDS','SDM College,Nair Dental College,MG \
Institute','670000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcb','BAMS','Tilak ayurveda college,Patanjali college,KG Mittal\
 college','860000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcb','BHMS','KUHS Thrissur,NTR University,Institute of\
Homeopathy','680000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcb','Physiotherapy','HIMSR college,IMS BHU,IPGMER \
kolkata','568000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcb','B.Sc Occupational Therapy','IMS BHU,HIMSR,GS Medical\
 college','670000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcb','B.Sc Nutriton','IGNOU,Institute of Nutrition,Amity University\
','570000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcb','B.Sc Bioinformatics','DAV college,Reva Univesity,\
Parul University','550000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcb','B.Sc Nursing','NIMS University,Madras Medica college,\
AIIMS','750000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcb','B.Sc Anthropology','University of Maysore,PRSU,IGNOU\
','470000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcb','B.Sc Microbiology','Gargi college,Fergusson college,\
st.xaviour college','540000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcb','B.Sc anaesthesia','AIIMS,IG Medical college,AMU','\
350000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcb','B.Sc Audiology','SRM college,AWH college,AIIMS','\
670000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcb','B.Sc Cardiology','Manipal University,AIIMS,Parul \
University','590000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('pcb','pharmacy','ICT Mumbai,CU Shah college,DD Vispute \
college','390000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('commerce','BCom','SRC college,LPU University,MCC Madras\
','569000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('commerce','C.A','Vidya sagar institute,MT Educate,Yeshas \
Academy','465000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('commerce','B.E','Fergussion college,Hansrak college,Loyola \
college','580000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('commerce','B.FA','Christ University,Madras college,Miranda \
house','470000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('commerce','B.Sc appied maths','IITT,CUTM,Flame University','\
590000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('commerce','B.Sc statisics','Loyola college,Farook college,\
Presidency college','360000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('commerce','BIBF','XLRI Jamshedpur,FMS BHU,UBS Chadigarh','\
570000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('commerce','BBA','NMIMS,Loyola college,Christ University','\
460000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('commerce','Company Secretary','ICSI Delhi,Elite IIT,Shiksha guru\
','340000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('commerce','B. tourism','NIT,Christ University,Institute of \
Tourism','250000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('commerce','B. Journalism','MOP college,MCC,Jai Hind \
college','480000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('commerce','B. Foreign trade','AP University,Prestige Institute,MCC\
','430000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('commerce','B. social work','Madras school,Tata Institute,IG \
University','510000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('arts','anchoring','IIMC,Delhi Film Institute,Apeejay Institute','\
320000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('arts','animation','NID Ahmedabad,MIT Institute,IDC IIT Bombay','\
730000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('arts','Multimedia','FAD Institute,MATS University,Pearl Academy\
','810000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('arts','B.A. Politica Sc','Amity University,IIS University,KK \
University','590000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('arts','B.A. Programme','LPU,IGNOU Delhi,Christ University','\
640000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('arts','B.A. Journalism','MCC,MOP college,St.Xavier college','\
587000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('arts','B.A. LLB','NLU Delhi,NLSIU Bangalore,SLS Pune','490000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('arts','B.A. English','Hindu College,MCM college,St.Xaviers college\
','495000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('arts','B.A. history','Hindu College,MCM college,St.Xaviers college\
','578000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('arts','B.A. Mass communication','MI College,St.Jay college,Khalsa\
College','782000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('arts','B.A. Philosophy','MCC,Christ University,Bethune College','\
623000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('arts','B.Des textile design','NID,NIFT delhi,Institute of fashion tech\
','624000'))
cur.execute("insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)", ('arts','B.Des fashion design','Pearl Academy,Amity University,MIT\
','860000'))
con.commit()
cur.close()
con.close()
'''
answ='y'
while (answ=='y'):
    user=input('what kind of user admin or student :')
    if user=='admin': #insert,delete,update
        usrnm=input('username=')
        pas=input('password=')
    
        con=myc.connect(host="localhost",user=usrnm,passwd=pas,database='project')
        cur=con.cursor()
        while True:
            print('Enter \n1:display all record \n2:insert a record \n3:delete a record \n4:update a record')
            ch=int(input('Enter your choice:'))
            if ch==1:
                print('[SUB STREAM,COURSES,TOP 3 COLLEGES,AVERAGE FEES]')
                cur.execute("select ucase(sub_stream),ucase(courses),ucase(top_3_colleges),ucase(average_fees) from substream order by sub_stream desc")
                i=cur.fetchall()
                head=("SUB STREAM","COURSES","TOP 3 COLLLEGES","AVERAGE FEE")
                print(tabulate(tabular_data=i,headers=head,tablefmt="grid"))

            elif ch==2:
                ct=int(input("how many records you want to insert : "))
                for i in range (1,ct+1):
                    print('record number:', i)
                    sbstrm=input('sub_stream:')
                    crs=input('course:')
                    tpcll=input('top 3 colleges:')
                    avgfee=int(input('average fees:'))
                    cur.execute('insert into substream(sub_stream,courses,top_3_colleges,average_fees) values(%s,%s,%s,%s)',(sbstrm,crs,tpcll,avgfee))
                    con.commit()

            elif ch==3:
                crs=input('enter course name to delete:')
                cur.execute('delete from substream where courses=%s',(crs,))
                con.commit()

            elif ch==4:
                while True:
                    print('select criteria to update= 1:top 3 colleges,2:average fees')
                    cr=int(input('your choice:'))
                    if cr==1:
                        crs=input('course to update:')
                        clgs=input('new college names: ')
                        cur.execute('update substream set top_3_colleges=%s where courses=%s',(clgs,crs))
                        con.commit()
                    elif cr==2:
                        crs=input('course to update:')
                        avgfee=int(input('new average fees: '))
                        cur.execute('update substream set average_fees=%s where courses=%s',(avgfee,crs))
                        con.commit()
                    else:
                        print('wrong choice')
                    ans=input('do you want to update more y/n:')
                    if ans=='y':
                        continue
                    else:
                        break
            else:
                print('wrong choice')
            anss=input('do you want to update more y/n:')
            if anss=='y':
                continue
            else:
                break        
                                                                                                                        
        cur.close()
        con.close()
    
    elif user=='student':
        con=myc.connect(host="localhost",user='root',passwd='pg262004',database='project')
        cur=con.cursor()
        ans='y'
        while ans=='y':
            print('1:search courses,2:fill form')
            ch=str(input())
            if ch=="search courses":
                    
                print('WHICH STREAM YOU WANT TO CONTINUE ON:')
                cur.execute("select ucase(stream) from streams")
                data1=cur.fetchall()
                print('STREAMS AVAILABLE:')
  
                for i in range(1,len(data1)+1):
                    print(i,'.',list(data1[i-1])[0])          
                print('STREAM YOU WANT TO CHOOSE')
                streams=input('STREAM=')

                cur.execute("select ucase(sub_stream) from streams where stream=%s",(streams,))
                data=cur.fetchall()
                print('SUB STREAMS AVAILABLE:')
  
                for i in range(1,len(data)+1):
                    print(i,'.',list(data[i-1])[0])          
                print('SUB STREAM YOU WANT TO CHOOSE')
                sub_stream=input('SUB STREAM=')

                cur.execute("select ucase(courses) from substream where sub_stream=%s",(sub_stream,))
                d=cur.fetchall()
                print('COURSES AVAILABLE FOR YOU:')
                for i in range(1,len(d)+1):
                    print(i,'.',list(d[i-1])[0])
  
                print('which course indormation you want')
                course=input('crse=')
                cur.execute("select top_3_colleges,average_fees from substream where courses=%s",(course,))
                x=cur.fetchall()
                for i in x:
                    print('top 3 colleges:',list(i)[0])
                    print('average fees:Rs',list(i)[1])        
            elif ch=="fill form":
                print('Please enter your details')
                nm=input('name:')
                gndr=input('M/F')
                brth=input('birth date:')
                adrs=input('address:')
                phn=int(input('phone number:'))
                prt=input('1st parnets name:')    
                ocps=input('occupation:')
                clphn=int(input('cell phone:'))
                email=input('email:')
                prt2=input('2nd parents name:')
                ocps2=input('occupation:')
                clphn2=int(input('cell phone:'))
                email2=input('email:')           
                print('Enter course related data:')            
                course=input('course you want to choose:')
                college=input('college you preffer:')
                dt=input('year you want to join')
                print('\n                          Student Enrollment Form')
            
                print('Name: ',nm,' Gender: ',gndr,' Birthdate: ',brth,'\nAddress: ',adrs,'\nPhone no: ',phn,'\n\n1st Parents Name: ',prt,'\nOccuation: ',ocps,' Cell Phone: ',clphn,\
                  '\nEmail Address: ',email,'\n\n2nd Parents Name: ',prt2,'\nOccupation: ',ocps2,' Cell Phone: ',clphn2,'\nEmail Address: ',email2,'\n\nThis Certifies that ',nm,\
                  'has enrolled his/her name\nfor Course: ',course,' in \nCollege: ',college,'\nfrom classes starting from year ',dt,'\n')
            
            ans=input('want to change your choce y/n')
            if ans=='n':
                break
        
        cur.close()
        con.close()
    answ=input('do you want to change user type y/n:')
    if answ=='n':
        break
    
