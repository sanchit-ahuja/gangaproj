'''Split the job into subjobs supplying all the splitted pdfs as subjobs '''

j=Job()
j.splitter=ArgSplitter()
j.application.exe = File('splitterjob.py')
j.splitter.attribute='application.args'
path='/home/sanchit/Desktop/gangaproj/'
for i in range(0,12):
    j.splitter.values.append(path+'document-page{}.txt'.format(i))

j.submit()