import os
# assign directory
directory = 'Writ Petition'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    f1=open(f,'r')
    # print(f)
    data=f1.read()
    data=data.replace("<JudgmentText>","<JudgmentText><P>")
    data=data.replace("</JudgmentText>","</P></JudgmentText>")
    data=data.replace("<P/>","</P><P>")
    data=data.replace("</I>","</P></I><P>")
    data=data.replace("<I>","</P><I><P>")
    data=data.replace("<Table>","</P><Table><P>")
    data=data.replace("</Table>","</P></Table><P>")
    f1.close()
    print(data)
    f1=open(f,"w")
    f1.write(data)