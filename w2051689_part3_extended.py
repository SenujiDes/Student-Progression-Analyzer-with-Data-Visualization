# I declare that my work contains no examples of misconduct, such as plagiarism,or any collusion orcollusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20230407
# Date: 11/12/2023



from graphics import *   #import the graphics.py module (must be in the same folder this file)

def inputvalidate(question): #this function validate integers , check whether it's out of range and resturn it to the main programme 
    while True:
        try:
            num=int(input(question))
        except:
            print("Integer required\n")
            continue
        if num in (0,20,40,60,80,100,120):
            break
        else:
            print("Out of range\n")
    return(num)

def draw_histogram(data):
    bar_width = 100
    max_value = max(data)
    scale_factor = 400 / max_value  # Adjust this factor based on your data range
    colors = ["palegreen","mediumseagreen","skyblue","plum"]
    barname = ["Prgress", "Trailer","Retriever","Excluded"]
    
    # Create a window
    win = GraphWin("Histogram", 800, 600)
    win.setBackground("Mint Cream")

    line= Line(Point(100,500) , Point(620,500))
    line.draw(win)

    total_count= 0 #initializing the total count of the progression

    for i, value in enumerate(data):
        x1 = i * (bar_width + 10) + 150 
        y1 = 500
        x2 = x1 + bar_width
        y2 = 500 - value * scale_factor

        total_count+= value

        #draw columns in the histogram
        bar = Rectangle(Point(x1, y1), Point(x2, y2)) 
        bar.setFill(colors[i]) # chose the color from colors list and fill the regatangle 
        bar.draw(win)

        # Display the value above each bar
        value_text = Text(Point((x1 + x2) / 2, y2 - 20), str(value)) # position where we should print the count of each progresssion (top of the column)
        value_text.setSize(20)
        value_text.setStyle("bold")
        value_text.draw(win)

        barname_text = Text(Point((x1 + x2) / 2, y1 + 20), barname[i]) #position of the bar names
        barname_text.setSize(13)
        barname_text.draw(win)

    label_text = Text(Point(400, 50), "Histogram Results") #printing the label (topic) of the histogram
    label_text.setSize(20)
    label_text.setStyle("bold")
    label_text.draw(win)
 
    total_text = Text(Point(250, 570), str(total_count)+ "  outcomes in total")
    total_text.setSize(20)
    total_text.draw(win)

    #Wait for a click before closing the window
    win.getMouse()
    win.close()

def continuation_string_validate(): #If the user didn't enter either y or q then , aware them to enter the correct command
    while True:
        ans=input("Enter 'y' for yes or 'q' to quit and view results:")
        if ans in ("y","q","Y","Q"):
            break
        else:
            print("Please enter 'y' or 'q' \n")
    return(ans)

def accesscodevalidate(): #to validate the access_code
    while True:
        try:
            num=int(input("Enter the access code:"))
        except:
            print("Integer required\n")
            continue
        if num in (1,2):
            break
        else:
            print("Please enter 1 or 2 \n")
    return(num)


# main programme 

progress_count=0
trailer_count=0
retriever_count=0
exclude_count=0

progression_list=[]
file= open("progression_file.txt","w")

print(" Student Access = 1 | Staff Access = 2 ")
access_code = accesscodevalidate()

multiple_student = "y" #As the while loop should be continued at least once 
while multiple_student == "y" or multiple_student == "Y":
    multiple_student = "q" #to make only staff memebers are allow to continue with multiple studnets.

    while True:
        pass_credit = inputvalidate("Please enter your credit at pass:")
        defer_credit = inputvalidate("Please enter your credit at defer:")
        fail_credit = inputvalidate("Please enter your credit at fail:")

        total_credit= pass_credit + defer_credit + fail_credit

        if total_credit == 120 :
            break
        else:
            print("Total incorrect\n")
            

    if pass_credit == 120:
        progression_outcome = "Progress"
        #print("Progress\n")
        progress_count+= 1

    elif pass_credit == 100:
        progression_outcome = "progress(Module trailer)"
        #print("Module trailer\n")
        trailer_count+=1

    elif (pass_credit + defer_credit) <= 40 :
        progression_outcome = "Exclude"
        #print("Exclude\n")
        exclude_count+=1
    else:
        progression_outcome = "Module retriever"
        #print("Module retriever\n")
        retriever_count+=1

    print(progression_outcome,"\n")
    current_progression_list = [progression_outcome,pass_credit,defer_credit,fail_credit]
    progression_list.append(current_progression_list)

    progress_text = str(progression_outcome)+" - "+str(pass_credit)+","+str(defer_credit)+","+str(fail_credit)+"\n"
    file.write(progress_text)

    if access_code == 2:
        print("Would you like to enter another set of data?")
        multiple_student= continuation_string_validate()
        print("\n")

file.close()

if access_code == 2:
    # data (progression outcome)
    progress_count_list = [progress_count, trailer_count, retriever_count, exclude_count]

    # Draw the histogram
    draw_histogram(progress_count_list)


    #printing a summery of stored data
    print("summery printing using lists\n")
    for item in progression_list:
        print(item[0], " - ", item[1], "," , item[2] , "," , item[3] )

    print("\n summery printing using files \n ")
    file=open("progression_file.txt","r")
    print(file.read())
    file.close()








