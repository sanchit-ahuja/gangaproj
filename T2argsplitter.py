'''Split the job into subjobs supplying all the splitted pdfs as subjobs using argsplitter'''

j=Job()
arg_list=[]
j.application.exe = File('splitterjob.py')
#j.splitter.attribute='application.args'
path='/home/sanchit/Desktop/gangaproj/TextFiles/'
for i in range(0,12):
    arg_list.append(path+'document-page{}.txt'.format(i))

for arg in arg_list:
    j.splitter=ArgSplitter(args=[arg])

j.submit()