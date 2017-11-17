import os, sys

# THIS SCRIPT REQUIRES CMSSW AND VOMS ENVIRONMENT

campaign="Moriond17"
datatier="MINIAODSIM"

crab_word = "" # put here your crab password
crab_user = "" # put here your crab user (the one that gets returned after voms etc etc)

xsec_script_folder="/your/folder/to/genproductions/test/calculateXSectionAndFilterEfficiency/" # change this folder

os.system("mkdir -p getXsec")

with open('datasets.txt') as f:
    for dataset in f:
        dataset = dataset.rstrip('\n')
        print dataset.split('/')[1]
        if not os.path.isfile("getXsec/getXsec_"+dataset.split('/')[1]+".sh"):
            print "Creating file"
            os.popen("sh getfiles/getfiles_"+dataset.split('/')[1]+".sh 2>&1 > getXsec/getXsec_"+dataset.split('/')[1]+".sh").read()
        else:
            with open("getXsec/getXsec_"+dataset.split('/')[1]+".sh", 'r+') as f:
                content = f.read()
                if not '/store' in content: 
                    print "File corrupted, creating file"
                    os.popen("sh getfiles/getfiles_"+dataset.split('/')[1]+".sh 2>&1 > getXsec/getXsec_"+dataset.split('/')[1]+".sh").read()
                else:
                    print "File found"
        os.system("chmod 755 getXsec/getXsec_"+dataset.split('/')[1]+".sh")
        
        # f1=open("xsec_"+dataset.split('/')[1]+"_getfiles.sh", 'w')
        # f1.write('python '+xsec_script_folder+'/compute_cross_section.py -f '+dataset+' -c '+campaign+' -n 100000 -d '+datatier+' --skipexisting "True"')
        # f1.close()
