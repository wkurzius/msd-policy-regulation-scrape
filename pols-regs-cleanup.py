import re, os
# import sys
# import os
# import glob

def cleanup(dir):
    for filename in os.listdir(dir):
        with open (os.path.join(dir, filename), 'r+',encoding="utf8") as f:
            content = f.read()
            
            content_new = re.sub('</p>','\n',content,flags=re.M)
            content_new = re.sub('<[^>]*>','',content_new,flags=re.M)
            content_new = re.sub('&#xa0;',' ',content_new,flags=re.M)
            content_new = re.sub('^\s+','',content_new,flags=re.M)
            # replacing consecutive spaces not currently working, skipped
            # content_new = re.sub('\s{2,}','',content_new,flags=re.M)
            content_new = re.sub('^$\n','',content_new,flags=re.M)
            content_new = re.sub('\.\s','.\n',content_new,flags=re.M)
            content_new = re.sub('^\s+','',content_new,flags=re.M)

            f.seek(0)
            f.write(content_new)
            f.truncate()

cleanup("D:\\GitHub\\msd-pols-regs\\pols")
cleanup("D:\\GitHub\\msd-pols-regs\\regs")
