jobs=[]
def addJob():
    job=input("What job do you want to add in the list? ")
    jobs.append(job)
    print(f"Job '{job}' is added in the list")

def delJob():
    viewJobs()
    n_jobTobeDeleted= int(input("\nEnter the number of job, you want to delete "))
    if n_jobTobeDeleted>0 and n_jobTobeDeleted< len(jobs):
        job_del = jobs.pop(n_jobTobeDeleted-1)
        print(f"The given job number {n_jobTobeDeleted} '{job_del}' is deleted")
    else:
        print(f"Job {n_jobTobeDeleted} does not exist")

def viewJobs():
    if not jobs:
        print("Job does not exist") 
    else:
        print("\nCURRENT JOBS")
        for index, job in enumerate(jobs):
            print(f"Job {index+1} {job} ")

while True:
    print("\nWEL COME TO-DO LIST MENU")
    print("***************************")
    print("1. Add Jobs")
    print("2. Delete Jobs")
    print("3. view Jobs")
    print("4. Exit")
    choice = input("Enter the choice number ")
    if choice == "1":
        addJob()
    elif choice=="2":
        delJob()
    elif choice == "3":
        viewJobs()
    elif choice == "4":
        break
    else:
        print("Invalid choice number!")
print("Bye Bye!!")

