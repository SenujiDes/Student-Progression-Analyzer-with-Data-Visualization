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

    value_count= 0

    for i, value in enumerate(data):
        x1 = i * (bar_width + 10) + 150 #
        y1 = 500
        x2 = x1 + bar_width
        y2 = 500 - value * scale_factor

        value_count+= value

        bar = Rectangle(Point(x1, y1), Point(x2, y2))
        bar.setFill(colors[i]) # chose the color from colors list and fill the regatangle 
        bar.draw(win)

        # Display the value above each bar
        value_text = Text(Point((x1 + x2) / 2, y2 - 20), str(value))
        value_text.setSize(20)
        value_text.setStyle("bold")
        value_text.draw(win)

        barname_text = Text(Point((x1 + x2) / 2, y1 + 20), barname[i])
        barname_text.setSize(13)
        barname_text.draw(win)

    label_text = Text(Point(400, 50), "Histogram Results")
    label_text.setSize(20)
    label_text.setStyle("bold")
    label_text.draw(win)
 
    total_text = Text(Point(250, 570), str(value_count)+ "  outcomes in total")
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

# main programme 

progress_count=0
trailer_count=0
retriever_count=0
exclude_count=0

multiple_student = "y"
while multiple_student == "y" or multiple_student == "Y" :

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
        print("Progress\n")
        progress_count+= 1

    elif pass_credit == 100:
        print("Progress(Module trailer)\n")
        trailer_count+=1

    elif (pass_credit + defer_credit) <= 40 :
        print("Exclude\n")
        exclude_count+=1
    else:
        print("Module retriever\n")
        retriever_count+=1
    
    print("Would you like to enter another set of data?")
    multiple_student= continuation_string_validate()


# data (progression outcome)
progress_count_list = [progress_count, trailer_count, retriever_count, exclude_count]

# Draw the histogram
draw_histogram(progress_count_list)








