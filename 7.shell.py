import subprocess

IOredirection=[">","<"]
piping="|"
while True:
    redirectionExist=False
    redirectionPostition=0
    standardIO=""
    pipingExist=False
    pipingPosition=0

    userinput=input("shell> ")
    str(userinput)
    command=userinput.strip().split(" ")

    for i in command:
        if i in IOredirection:
            redirectionPostition=command.index(i)
            redirectionExist=True
            standardIO=i
        if i == piping:
            pipingPosition=command.index(i)
            pipingExist=True


    if redirectionExist:
        arg1=[]
        arg2=[]
        for i in range(0,redirectionPostition):
            arg1.append(command[i])
        for i in range(redirectionPostition+1,len(command)):
            arg2.append(command[i])
        """print(arg1)
        print(arg2)"""
        if standardIO == ">": #Redirect output
            try:
                process=subprocess.Popen(arg1,stdout=subprocess.PIPE,text=True).communicate()
                with open(arg2[0],"w") as file:
                    file.write(process[0])
            except:
                print("Error! something went wrong")
        if standardIO == "<": #Redirect input
            try:
                with open(arg2[0],"r") as file:
                    data=file.read().encode("utf-8")
                process=subprocess.Popen(arg1,stdin=subprocess.PIPE).communicate(data)
            except:
                print("Error! something went wrong")

    elif pipingExist:
        arg1=[]
        arg2=[]
        for i in range(0,pipingPosition):
            arg1.append(command[i])
        for i in range(pipingPosition+1,len(command)):
            arg2.append(command[i])
        """print(arg1)
        print(arg2)"""
        try:
            firstProcess=subprocess.Popen(arg1,stdout=subprocess.PIPE)
            secondProcess=subprocess.Popen(arg2,stdin=firstProcess.stdout).wait()
        except:
            print("Error! something went wrong")

    else:
        if command==[""]:
            continue
        elif command!=["exit"]:
            try:
                subprocess.run(command)
            except:
                print("Error! something went wrong")
        else:
            break
        