
j=Job()
j.splitter=GenericSplitter()
j.application.exe = File('splitterjob.py')
j.splitter.attribute='application.args'
path='/home/sanchit/Desktop/gangaproj/PDFiles/'
for i in range(0,12):
    j.splitter.values.append(path+'document-page{}.pdf'.format(i))
j.postprocessors.append(CustomMerger(module='/home/sanchit/Desktop/gangaproj/merger.py',files=['stdout']))
j.submit()