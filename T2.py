'''Split the job into subjobs supplying all the splitted pdfs as subjobs using a GenericSplitter '''

j=Job()
j.splitter=GenericSplitter()
j.application.exe = File('splitterjob.py')
j.splitter.attribute='application.args'
path='//gangaproj/PDFiles/'
for i in range(0,12):
    j.splitter.values.append(path+'document-page{}.pdf'.format(i))

j.submit()