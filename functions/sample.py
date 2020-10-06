#coding:utf-8

import os
import random
import shutil
import numpy

# Creation of a sample of emails among all the emails.

def create_sample (sample_size, number_of_sample) :
    print(f"Creation of {number_of_sample} samples each contening {sample_size} emails.")

# Definition of the different directories.

    dirname = os.getcwd()
    mailDir = os.path.join(dirname,'maildir')

# Counting emails.

    mails_count = sum(len(files) for _, _, files in os.walk(mailDir)) 
    print(f"The maildir folder contains {mails_count} emails.")

# Cleaning the target file.

    shutil.rmtree(os.path.join(dirname,'sample'))

    for sample in range(1, number_of_sample+1) :
        print (f"Sample number {sample}.")
        sampleDir = os.path.join(dirname,'sample', str(sample))

        if not os.path.exists(sampleDir):
            os.makedirs(sampleDir)

        # Draw random emails and copy them to the sample folder.
        
        random_list = numpy.random.randint(1,mails_count+1,sample_size)
        print(len(random_list))
        id_mail = 1
        for repertory, sub_repertory, files in os.walk(mailDir):
            for f in files :
                if id_mail in random_list :
                    shutil.copy(os.path.join(repertory, f), sampleDir)
                    os.rename(os.path.join(sampleDir, f),os.path.join(sampleDir, str(id_mail)))
                id_mail +=1
        print (f"Creation of the sample {sample} successfully completed.")
        print (f"{sample_size} random mails have been copied to target repertory.")
    
    print (f"OK - {number_of_sample} samples of {sample_size} emails created in target repertory.")


create_sample(10000, 1)