from Staff import Staff

staff_member_one = Staff(1, "Sarah", "Parker", "S.P@Place.cam", "Nurse")

staff_member_one.add_patient_to_start("Phil")
staff_member_one.add_patient_to_end("Jeff")

staff_member_one.remove_patient_from_start()
staff_member_one.show_all_patients()

