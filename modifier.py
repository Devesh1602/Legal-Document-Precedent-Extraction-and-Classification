#This is the first model made depending on Act *no.* or *no.* Act logic

import xml.etree.ElementTree as ET
import os

directory = 'Writ Petition'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    mytree = ET.ElementTree(file= f)
    myroot = mytree.getroot()

    out_dir = directory+' output'
    out_file = os.path.join(out_dir, filename.replace(".xml", " output.txt"))
    out = open( out_file, 'w')
    for i in myroot:
        #if i.tag =='Laws' :
        # out.write("Root Tags : " + i.tag + '\n')
        if(i.tag=='JudgmentText'):
            for legis in i:
                # out.write("Inside Judgement Text : " + legis.tag + '\n')
                if(legis.tag=='I'):
                    for para in legis:
                        # out.write(para.text + '\n\n')
                        if para.text is None:
                            continue
                        x = para.text.split()
                        for i in range(len(x)):
                            if(x[i].replace(",","").lower() == "act"):
                                if (i!=0 and x[i-1].replace(",","").isnumeric()) or (i!=len(x)-1 and x[i+1].replace(",","").isnumeric()):
                                    out.write("Legislation : " + para.text + '\n\n')
                                    break

                elif(legis.tag=='P'):
                    # print(len(legis))
                    # if(len(legis)):
                    #     print(len(legis))
                    #     print({x.tag for x in legis.findall(i.tag + "/*")})

                    # print(legis.text)

                    if legis.text is None:
                        continue

                    x = legis.text.split()
                    for i in range(len(x)):
                        if(x[i].replace(",","").lower() == "act"):
                            if (i!=0 and x[i-1].replace(",","").isnumeric()) or (i!=len(x)-1 and x[i+1].replace(",","").isnumeric()):
                                out.write("Statute : " + legis.text + '\n\n')
                                break