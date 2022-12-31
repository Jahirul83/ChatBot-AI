import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_Greating = "WalikumAssalam, How can I help you?"
Uni_Ranking = "IIUC is 24th among Bangladeshi University"
Uni_tot_dept = "there is 10 department in IIUC, such as cse,eee,etc,cce,bba,civil,ell,qsis,hadith,llb,pharmacy,economic & banking"
cse_chairman_no = "01788378741"
reg_no = "073253327"
admission_link = "http//:iiuc.ac.bd/admission"
location = "Kumira, Chattagram,Bangladesh"
hostel = "Yes, IIUC have hostel facilities"
min_gpa_EP= "for Faculty of Science & Engineering & Pharmacy the minimum gpa is required 3.50"
min_gpa_ell="for Faculty of ELL the minimum gpa is required 2.50"
min_gpa_econ="for Faculty of Economic & Banking  and BBA, the minimum gpa is required 3.50"
min_gpa_law="for Faculty of LAW, the minimum gpa is required 3.00"
cost_eng = "Cost for Faculty of Science & Engineering is around 600000 BDT"
cost_parma = "Cost for Faculty of Pharmacy is around 650000 BDT"
cost_econ = "Cost for Faculty of Economic & Banking is around 450000 BDT"
cost_law = "Cost for Faculty of LAW is around 500000 BDT"
cost_ell = "Cost for Faculty of ELL is around 350000 BDT"
cost_arabic = "Cost for Faculty of Arabic & Islamic Studies is around 100000 BDT"
library = "There is a large library in IIUC"
cafe = "There is a large cafeteria in IIUC"
two_campus = "The campus is different for boys & girls"
transport = "IIUC has it's own transportation facility for teacher, stuffs & students"
admission_fee="Admission Fee is around 30000"
waiver = "IIUC has different kinds of waiver for more information goto this link: http//:iiuc.ac.bd/waiver"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(6)]
    return response
