from tkinter import *
from PIL import ImageTk,Image


def workout_Menu ():
    print("---Welcome to your Workout Planner, Please select from the following options----")

    print("[1] Arm Workout")
    print("[2] Legs Workout")
    print("[3] Back Workout")
    print("[4] Chest Workout")
    print("[5] Full Body Workout")
    print("[6] Cardio and Hiit")
    print("[7] Workout Library")
    print("[0] Exit")

workout_Menu()
workout = int(input("Please Select a workout: "))


def Arm_Workout():
    root = Tk()
    root.title('Arms Workout')

    my_img = ImageTk.PhotoImage(Image.open("/Users/samidollars/Desktop/github_projects/workout_app/"
                                           "/Image/arms.jpeg"))

    my_label = Label(image=my_img)
    my_label.pack()


    root.mainloop()


def Legs_Workout():
    root = Tk()
    root.title('Legs Workout')

    my_img = ImageTk.PhotoImage(Image.open("/Users/samidollars/Desktop/github_projects/workout_app/"
                                           "/Image/legs.jpeg"))


    my_label = Label(image=my_img)
    my_label.pack()

    root.mainloop()



def Back_Work():
    root = Tk()
    root.title('Back Workout')

    my_img = ImageTk.PhotoImage(Image.open("/Users/samidollars/Desktop/github_projects/workout_app/"
                                           "/Image/back.jpeg"))
    my_label = Label(image=my_img)
    my_label.pack()

    root.mainloop()

def Chest_Workout():
    root = Tk()
    root.title('Chest Workout')

    my_img = ImageTk.PhotoImage(Image.open("/Users/samidollars/Desktop/github_projects/workout_app/"
                                           "/Image/chest.jpeg"))
    my_label = Label(image=my_img)
    my_label.pack()

    root.mainloop()

def Full_Body():
    root = Tk()
    root.title('Full Body Workout')

    my_img = ImageTk.PhotoImage(Image.open("/Users/samidollars/Desktop/github_projects/workout_app/"
                                           "/Image/fullbody.jpeg"))
    my_label = Label(image=my_img)
    my_label.pack()

    root.mainloop()


def Cardio_Hiit():
    root = Tk()
    root.title('Cardio_Hiit')

    my_img = ImageTk.PhotoImage(Image.open("/Users/samidollars/Desktop/github_projects/workout_app/"
                                           "/Image/100-hiit-collection.jpeg"))
    my_label = Label(image=my_img)
    my_label.pack()

    root.mainloop()



if __name__ == '__main__':


    while workout != 0:

        if workout == 1:
            Arm_Workout()


        elif workout == 2:
             Legs_Workout()

        elif workout == 3:
             Back_Work()

        elif workout == 4:
            Chest_Workout()

        elif workout == 5:
            Full_Body()

        elif workout == 6:
            Cardio_Hiit()

        elif workout == 7:
            root = Tk()
            root.title('Workout Library')

            arms_workout = ImageTk.PhotoImage(Image.open("/Users/samidollars/Desktop/github_projects/workout_app/"
                                           "/Image/arms.jpeg"))

            legs_workout = ImageTk.PhotoImage(Image.open("/Users/samidollars/Desktop/github_projects/workout_app/"
                                           "/Image/legs.jpeg"))

            back_workout = ImageTk.PhotoImage(Image.open("/Users/samidollars/Desktop/github_projects/workout_app/"
                                           "/Image/back.jpeg"))

            chest_workout = ImageTk.PhotoImage(
                Image.open("/Users/samidollars/Desktop/github_projects/workout_app/"
                                           "/Image/chest.jpeg"))

            full_body_workout = ImageTk.PhotoImage(
                Image.open("/Users/samidollars/Desktop/github_projects/workout_app/"
                                           "/Image/fullbody.jpeg"))

            cardio_hiit_workout = ImageTk.PhotoImage(
                Image.open("/Users/samidollars/Desktop/github_projects/workout_app/"
                                           "/Image/100-hiit-collection.jpeg"))

            image_list = [arms_workout, legs_workout, back_workout, chest_workout, full_body_workout,
                          cardio_hiit_workout]

            my_label = Label(image=arms_workout)
            my_label.grid(row=0, column=0, columnspan=3)


            def forward(image_number):
                global my_label
                global button_forward
                global button_back

                my_label.grid_forget()
                my_label = Label(image=image_list[image_number - 1])
                button_forward = Button(root, text="Forward>>", command=lambda: forward(image_number + 1))
                button_back = Button(root, text="<<Back", command=lambda: back(image_number - 1))

                if image_number == 6:
                    button_forward = Button(root, text=">>", state=DISABLED)

                my_label.grid(row=0, column=0, columnspan=3)
                button_back.grid(row=1, column=0)
                button_forward.grid(row=1, column=2)


            def back(image_number):
                global my_label
                global button_forward
                global button_back

                my_label.grid_forget()
                my_label = Label(image=image_list[image_number - 1])
                button_forward = Button(root, text="Forward>>", command=lambda: forward(image_number + 1))
                button_back = Button(root, text="<<Back", command=lambda: back(image_number - 1))

                if image_number == 1:
                    button_back = Button(root, text="<<", state=DISABLED)

                my_label.grid(row=0, column=0, columnspan=3)
                button_back.grid(row=1, column=0)
                button_forward.grid(row=1, column=2)


            button_back = Button(root, text="<<Back", command=back, state=DISABLED)

            button_forward = Button(root, text="Forward>>", command=lambda: forward(2))

            button_back.grid(row=1, column=0)

            button_forward.grid(row=1, column=2)

            root.mainloop()



        else:
            print("INVALID ENTRY PLEASE ENTER A NUMBER FROM 1 TO 7 TO SELECT AN EXERCISE AND 0 TO QUIT")

        workout_Menu()
        workout = int(input("Please Select a workout: "))






print("Thank you for your visit we hope to see you soon")