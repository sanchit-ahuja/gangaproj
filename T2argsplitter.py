'''Split the job into subjobs supplying all the splitted pdfs as subjobs using argsplitter'''

j=Job()
arg_list=[]
j.application.exe = File('splitterjob.py')
#j.splitter.attribute='application.args'
path='/home/sanchit/Desktop/gangaproj/PDFiles/'
for i in range(0,12):
    arg_list.append(path+'document-page{}.pdf'.format(i))

arg_supply=[]
for arg in arg_list:
    arg_supply.append([arg])
j.splitter=ArgSplitter(args=arg_supply)
j.submit()