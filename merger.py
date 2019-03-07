'''Split the job into subjobs supplying all the splitted pdfs as subjobs using a GenericSplitter '''

import os
def mergefiles(file_list,output_file):
    f_out=file(output_file,'w')
    cnt=0
    for f in file_list:
        f_in=file(f)
        cnt+=int(str(f_in.read().strip()))
        f_in.close()
    f_out.write(cnt)
    f_out.flush()
    f_out.close()
    if f_out:
        return 0
    else:
        return -1
