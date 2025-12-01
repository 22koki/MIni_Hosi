import sqlite3

# -----------------------------
# 1. Connect to SQLite database
# -----------------------------
conn = sqlite3.connect('HealthClinic.db')
cursor = conn.cursor()

# Enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON;")

# -----------------------------
# 2. CREATE (Insert new data)
# -----------------------------
# Add a new patient
cursor.execute("""
INSERT INTO Patient (Full_Name, Age, Gender, Contact_Number, Address, Medical_History)
VALUES (?, ?, ?, ?, ?, ?)
""", ("Brian Otieno", 35, "Male", "0722001122", "Mombasa", "Allergic to penicillin"))

# Add a new doctor
cursor.execute("""
INSERT INTO Doctor (Full_Name, Specialty, Contact_Number, Email)
VALUES (?, ?, ?, ?)
""", ("Dr. Mary Njeri", "Pediatrician", "0711223344", "mary@example.com"))

conn.commit()
print("✅ Created new patient and doctor.")

# -----------------------------
# 3. READ (Query data)
# -----------------------------
# Get all patients
cursor.execute("SELECT * FROM Patient")
patients = cursor.fetchall()
print("\nAll Patients:")
for p in patients:
    print(p)

# Get appointments for patient ID 1
cursor.execute("""
SELECT a.Appointment_ID, a.Appointment_Date, d.Full_Name AS Doctor
FROM Appointment a
JOIN Doctor d ON a.Doctor_ID = d.Doctor_ID
WHERE a.Patient_ID = ?
""", (1,))
appointments = cursor.fetchall()
print("\nAppointments for Patient ID 1:")
for a in appointments:
    print(a)

# -----------------------------
# 4. UPDATE (Modify existing data)
# -----------------------------
# Update patient contact number
cursor.execute("""
UPDATE Patient
SET Contact_Number = ?
WHERE Patient_ID = ?
""", ("0700112233", 1))
conn.commit()
print("\n✅ Updated Patient ID 1 contact number.")

# Update medicine stock after usage
cursor.execute("""
UPDATE Medicine
SET Stock_Level = Stock_Level - ?
WHERE Medicine_ID = ?
""", (2, 1))
conn.commit()
print("✅ Updated Medicine stock.")

# -----------------------------
# 5. DELETE (Remove data)
# -----------------------------
# Delete a patient (Patient_ID = 2)
cursor.execute("DELETE FROM Patient WHERE Patient_ID = ?", (2,))
conn.commit()
print("\n✅ Deleted Patient ID 2 if exists.")

# Delete a specific appointment
cursor.execute("DELETE FROM Appointment WHERE Appointment_ID = ?", (1,))
conn.commit()
print("✅ Deleted Appointment ID 1 if exists.")

# -----------------------------
# 6. Close connection
# -----------------------------
conn.close()
print("\n✅ Database connection closed.")
