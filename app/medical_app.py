from database_manager import *
from pathlib import Path

#from tkinter import *
# Explicit imports to satisfy Flake8
#Add a funciton where when a database is edited, clear the predicted medical cost
#Add an are u sure you want to delete button
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Menu, messagebox
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets"
print(OUTPUT_PATH)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / path



window = Tk()

window.geometry("1325x960")
window.configure(bg = "#FFFFFF")
window.title("Medical Cost Predictor")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 960,
    width = 1325,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

def show_information_popup():
    messagebox.showinfo("Information", "To create a new record, clear, type entries, then click new.\nTo delete a record, click delete.\nTo edit a new record, simply edit the record then click edit.")

def confirm_exit():
    response = messagebox.askyesno("Exit", "Are you sure you want to quit?")
    if response:
        window.quit()

menubar = Menu(window)
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="Instructions", command=lambda: show_information_popup())
menubar.add_cascade(label="Help", menu=help_menu)
menubar.add_command(label="Exit", command=confirm_exit)

window.config(menu=menubar)



db = DatabaseManager()

connectToDatabaseImage = PhotoImage(file=relative_to_assets("connectToDatabase.png"))
entry = PhotoImage(file=relative_to_assets("entry.png"))
deleteImage = PhotoImage(file=relative_to_assets("delete.png"))
disconnectDatabaseImage = PhotoImage(file=relative_to_assets("disconnectDatabase.png"))
editImage = PhotoImage(file=relative_to_assets("edit.png"))
left1Image = PhotoImage(file=relative_to_assets("left1.png"))
left2Image = PhotoImage(file=relative_to_assets("left2.png"))
left3Image = PhotoImage(file=relative_to_assets("left3.png"))
leftEndImage = PhotoImage(file=relative_to_assets("leftEnd.png"))
newImage = PhotoImage(file=relative_to_assets("new.png"))
right1Image = PhotoImage(file=relative_to_assets("right1.png"))
right2Image = PhotoImage(file=relative_to_assets("right2.png"))
right3Image = PhotoImage(file=relative_to_assets("right3.png"))
rightEndImage = PhotoImage(file=relative_to_assets("rightEnd.png"))
clearImage = PhotoImage(file=relative_to_assets("clear.png"))
predictAnnualCostImage = PhotoImage(file=relative_to_assets("predictAnnualCost.png"))
unresizedLogo = Image.open(relative_to_assets("image.png"))
resizedLogo = unresizedLogo.resize((200, 200))
logo = ImageTk.PhotoImage(resizedLogo)

#Left Border Rectangle
canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    250.0,
    960.0,
    fill="#919191",
    outline="")

#Central Rectangle
canvas.create_rectangle(
    272.000244140625,
    188.0,
    1304.000244140625,
    760.0,
    fill="#B2B1B1",
    outline="")

canvas.create_text(
    419.000244140625,
    29.0,
    anchor="nw",
    text="Medical Cost Machine Learning - Database",
    fill="#000000",
    font=("Inter ExtraBold", 32 * -1)
)

canvas.create_text(
    362.000244140625,
    222.0,
    anchor="nw",
    text="BMI:",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    333.000244140625,
    301.0,
    anchor="nw",
    text="Diabetes:",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    292.000244140625,
    380.0,
    anchor="nw",
    text="Hypertension:",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    280,
    456.0,
    anchor="nw",
    text="Heart Disease:",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    333.000244140625,
    531.0,
    anchor="nw",
    text="Asthma:",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    312.000244140625,
    610.0,
    anchor="nw",
    text="Daily Steps:",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    304.000244140625,
    689.0,
    anchor="nw",
    text="Sleep Hours:",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    851.000244140625,
    224.0,
    anchor="nw",
    text="Stress Level:",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    759.000244140625,
    301.0,
    anchor="nw",
    text="Annual Doctor Visits:",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    759.000244140625,
    380.0,
    anchor="nw",
    text="Hospital Admissions:",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    789.000244140625,
    456.0,
    anchor="nw",
    text="Medication Count:",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    729.000244140625,
    530,
    anchor="nw",
    text="Insurance Coverage pct:",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    767.000244140625,
    610.0,
    anchor="nw",
    text="Previous Year Cost:",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    726.000244140625,
    692.0,
    anchor="nw",
    text="Predicted Annual Medical Cost:",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

#>>> Button
left3Button = Button(
    image=right3Image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [db.right3(), db.update_screen(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry)],
    relief="flat",
    bg="#FFFFFF",
    activebackground="#FFFFFF"
)
left3Button.place(
    x=993.000244140625,
    y=820.0
)
#>| Button
rightEndButton = Button(
    image=rightEndImage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [db.rightEnd(), db.update_screen(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry, canvas, patient_id_text)],
    relief="flat",
    bg="#FFFFFF",
    activebackground="#FFFFFF"
)
rightEndButton.place(
    x=1085.000244140625,
    y=820.0
)
#>> Button
right2Button = Button(
    image=right2Image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [db.right2(), db.update_screen(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry, canvas, patient_id_text)],
    relief="flat",
    bg="#FFFFFF",
    activebackground="#FFFFFF"
)
right2Button.place(
    x=901.000244140625,
    y=820.0
)
#> Button
right1Button = Button(
    image=right1Image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [db.right1(), db.update_screen(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry, canvas, patient_id_text)],
    relief="flat",
    bg="#FFFFFF",
    activebackground="#FFFFFF"
)
right1Button.place(
    x=809.000244140625,
    y=820.0
)
#< Button
left1Button = Button(
    image=left1Image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [db.left1(), db.update_screen(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry, canvas, patient_id_text)],
    relief="flat",
    bg="#FFFFFF",
    activebackground="#FFFFFF"
)
left1Button.place(
    x=683.000244140625,
    y=820.0
)
#Connect to Database Button
connectToDatabaseButton = Button(
    image=connectToDatabaseImage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [db.open(), db.update_screen(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry, canvas, patient_id_text)],
    relief="flat",
    bg="#919191",
    activebackground="#919191"
)
connectToDatabaseButton.place(
    x=10.0,
    y=181.0
)

#Disconnect Database Button
disconnectDatabaseButton = Button(
    image=disconnectDatabaseImage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: db.close(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry, canvas, patient_id_text),
    relief="flat",
    bg="#919191",
    activebackground="#919191"
)
disconnectDatabaseButton.place(
    x=10.0,
    y=261.0
)
#|< Button
leftEndButton = Button(
    image=leftEndImage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [db.leftEnd(), db.update_screen(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry, canvas, patient_id_text)],
    relief="flat",
    bg="#FFFFFF",
    activebackground="#FFFFFF"
)
leftEndButton.place(
    x=407.000244140625,
    y=820.0
)
#<< Button
left2Button = Button(
    image=left2Image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [db.left2(), db.update_screen(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry, canvas, patient_id_text)],
    relief="flat",
    bg="#FFFFFF",
    activebackground="#FFFFFF"
)
left2Button.place(
    x=591.000244140625,
    y=820.0
)
#<<< Button
left3Button = Button(
    image=left3Image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [db.left3(), db.update_screen(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry)],
    relief="flat",
    bg="#FFFFFF",
    activebackground="#FFFFFF"
)
left3Button.place(
    x=499.000244140625,
    y=820.0
)
#BMI Entry
'''entry_bg_1 = canvas.create_image(
    470.000244140625, 211.0,
    image=entry
)'''
bmiEntry = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Arial", 18)
)
bmiEntry.place(
    x=470.000244140625, y=211.0,
    width=220.0, height=41.0
)

#Diabetes Entry
diabetesEntry = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Arial", 18)
)
diabetesEntry.place(
    x=470.000244140625, y=290.0,
    width=220.0, height=41.0
)

#Hypertension Entry
hypertensionEntry = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Arial", 18)
)
hypertensionEntry.place(
    x=470.000244140625, y=368.0,
    width=220.0, height=41.0
)
#Heart Disease Entry
heartDiseaseEntry = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Arial", 18)
)
heartDiseaseEntry.place(
    x=470.000244140625, y=447.0,
    width=220.0, height=41.0
)
#Asthma Entry
asthmaEntry = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Arial", 18)
)
asthmaEntry.place(
    x=470.000244140625, y=520.0,
    width=220.0, height=41.0
)
#Daily Steps Entry
dailyStepsEntry = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Arial", 18)
)
dailyStepsEntry.place(
    x=470.000244140625, y=599.0,
    width=220.0, height=41.0
)
#Sleep Hours Entry
sleepHoursEntry = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Arial", 18)
)
sleepHoursEntry.place(
    x=470.000244140625, y=677.0,
    width=220.0, height=41.0
)
#Stress Levels Entry
stressLevelsEntry = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Arial", 18)
)
stressLevelsEntry.place(
    x=1035.000244140625, y=213.0,
    width=220.0, height=41.0
)
#Annual Doctor Visits Entry
annualDoctorVisitsEntry = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Arial", 18)
)
annualDoctorVisitsEntry.place(
    x=1035.000244140625, y=291.0,
    width=220.0, height=41.0
)
#Hospital Admissions Entry
hospitalAdmissionsEntry = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Arial", 18)
)
hospitalAdmissionsEntry.place(
    x=1035.000244140625, y=369.0,
    width=220.0, height=41.0
)
#Medication Count Entry
medicationCountEntry = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Arial", 18)
)
medicationCountEntry.place(
    x=1035.000244140625, y=443.0,
    width=220.0, height=41.0
)
#Insurance Coverage pct Entry
insuranceCoverageEntry = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Arial", 18)
)
insuranceCoverageEntry.place(
    x=1035.000244140625, y=521.0,
    width=220.0, height=41.0
)
#Previous Year Cost Entry
previousYearCostEntry = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Arial", 18)
)
previousYearCostEntry.place(
    x=1035.000244140625, y=599.0,
    width=220.0, height=41.0
)
#Predicted Annual Medical Cost Entry
predictedAnnualMedicalCostEntry = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    state="readonly",
    font=("Arial", 18)
)
predictedAnnualMedicalCostEntry.place(
    x=1101.000244140625, y=681.0,
    width=190.0, height=41.0
)
#New Button
newButton = Button(
    image=newImage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: 
        [db.inserting(bmiEntry.get(), diabetesEntry.get(), hypertensionEntry.get(), heartDiseaseEntry.get(), asthmaEntry.get(), dailyStepsEntry.get(), sleepHoursEntry.get(), stressLevelsEntry.get(), annualDoctorVisitsEntry.get(), hospitalAdmissionsEntry.get(), medicationCountEntry.get(), insuranceCoverageEntry.get(), previousYearCostEntry.get()), db.update_screen(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry, canvas, patient_id_text)],
    relief="flat",
    bg="#919191",
    activebackground="#919191"
)
newButton.place(
    x=79.0,
    y=341.0
)
#Edit Button
editButton = Button(
    image=editImage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:
        [db.editing(bmiEntry.get(), diabetesEntry.get(), hypertensionEntry.get(), heartDiseaseEntry.get(), asthmaEntry.get(), dailyStepsEntry.get(), sleepHoursEntry.get(), stressLevelsEntry.get(), annualDoctorVisitsEntry.get(), hospitalAdmissionsEntry.get(), medicationCountEntry.get(), insuranceCoverageEntry.get(), previousYearCostEntry.get()), db.update_screen(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry, canvas, patient_id_text)],
    relief="flat",
    bg="#919191",
    activebackground="#919191"
)
editButton.place(
    x=79.0,
    y=430.0
)
#Delete Button
deleteButton = Button(
    image=deleteImage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [db.delete(), db.update_screen(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry, canvas, patient_id_text)],
    relief="flat",
    bg="#919191",
    activebackground="#919191"
)
deleteButton.place(
    x=79.0,
    y=519.0
)
#Clear Entries Button
clearEntriesButton = Button(
    image=clearImage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: db.clear(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry,predictedAnnualMedicalCostEntry, canvas, patient_id_text),
    relief="flat",
    bg="#919191",
    activebackground="#919191"
)
clearEntriesButton.place(
    x=79.0,
    y=610.0
)
#predictAnnualCost Button
predictAnnualCostButton = Button(
    image=predictAnnualCostImage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [db.input_prediction(), db.update_screen(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry, canvas, patient_id_text)],
    relief="flat",
    bg="#FFFFFF",
    activebackground="#FFFFFF"
)
predictAnnualCostButton.place(
    x=660.000244140625,
    y=890.0
)
#klw25 rectangle
canvas.create_rectangle(
    27.0,
    29.0,
    222.0,
    146.0,
    fill="#D9D9D9",
    outline="")

patient_id_text = canvas.create_text(
    50.0,
    76.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Inter SemiBold", 25 * -1)
)

canvas.create_rectangle(
    246.99853515625,
    95.76166534423828,
    1325.0013427734375,
    98.76166534423828,
    fill="#000000",
    outline="")

#Line
canvas.create_rectangle(
    245.0,
    -3.0,
    250.0,
    962.0,
    fill="#000000",
    outline="")

#Line
canvas.create_rectangle(
    707.00024417336,
    185.0000334991346,
    711.000244140625,
    761.0,
    fill="#000000",
    outline="")

#Line
canvas.create_rectangle(
    726.000244140625,
    654.0,
    1247.000244140625,
    657.0,
    fill="#000000",
    outline="")

#Image
canvas.create_image(
    125.0,
    810.0,
    image=logo
)
window.resizable(False, False)
window.mainloop()
