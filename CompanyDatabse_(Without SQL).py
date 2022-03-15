"""Making a company databse where you can store the data of clients and as well as the data of the workers"""

allowed_ids = {                                                         #Code will use the keys of this dict as id for security check.
               100:'Amaan',
               110:'Suresh',
               111:'Avdesh'
              }

worker_data = {
        'Amaan': 'Coder',
        'Rohit': 'Tester',
        'Ankur': 'System Analyst' }
                                                                        #If The security check passes then the worker and cliet_data data can be access or modified.
client_data = {
        'Mr Amitpal': 'Data Prediction',
        'Mr Avdesh': 'Web Backend Devlopment',
        'Mr Nitin ': 'Product Secuirty' }

class Company_Databse:                                                   #Making and naming the class as 'company database'.

     #def __init__(self,ask_data,your_id):
        # self.ask = ask_data                                             #ask_data for worker,client and add command selection.
        # self.id = your_id                                               #your_id for comapring the inputted id from allowed ids.

     def security_check_op(self,pass_id):                                           #Method for checking the id and printing the name attached to the id.
         if pass_id == 100:
            print('Hello Welcome Back', allowed_ids[100].title())

         elif pass_id == 110:
            print('Hello Welcome Back', allowed_ids[110].title())

         elif pass_id == 111:
            print('Hello Welcome Back', allowed_ids[111].title())

         else:
            permit_fail = True
            if permit_fail == True:                                     #if id not in series of condition then code will exit
                print('\n','Incorrect Id Permission Denied..!!')
                exit()

     def worker_database_outer_op(self):
         print('You are in now Workers Information Databse')
         ask_data_access = input('\n' + 'Want (Names,Position or All) Info:')

         if ask_data_access.lower() == 'names':
            for names in worker_data.keys():
                print(names.title())

         elif ask_data_access.lower() == 'position':
            for position in worker_data.values():
                print(position.title())

         elif ask_data_access.lower() == 'all':
            x=1
            print('\n')
            for name,position in worker_data.items():
                print(x,'-'+'The Names is ' + name + ' Is ' + position)
            x+=1

     def client_database_outer_op(self):
         print('You are in now Client Information Databse')
         ask_data_access = input('Want (Names,Projects or All) Info:')
         if ask_data_access.lower() == 'names':
            print('The Names Of Our Clients Are:')
            for names in client_data.keys():
                print(names.title())

         elif ask_data_access.lower() == 'projects':
            print('[+] These Projects Company Dealing On.')
            for project in client_data.values():
                print(project.title())

         elif ask_data_access.lower() == 'all':
            for name,project in worker_data.items():
                print('The Names is ' + name + ' And Project Is ' + project)

         else:
            print('\n','Invalid Command','Please Choose The Correct Data Type..!!')
            exit()

     def adding_data_under_op(self):
         ask_add = input('Want to Add Data in Worker Or Client Database:')
         if ask_add.lower() == 'worker':
            name_worker = input('Enter the name of worker:')
            worker_desgination = input('Enter the post:')
            worker_data[name_worker.title()] = worker_desgination.title()

         elif ask_add.lower() == 'client':
            client_name = input('Enter the name of worker:')
            project_assigned = input('Enter the post:')
            client_data[client_name.title()] = project_assigned.title()
         else:
            print('Invalid command..!!')

     def finding_data_under_op(self):
        ask_find = input('Want to find the data in client or worker database:')
        if ask_find.lower() == 'worker':

            ask_find_name_w = input('Enter the name:')
            for name in worker_data.keys():
                if name == ask_find_name_w.title():
                    print('Data Is Available ' + 'Name: ' + name.title() + ' Designation: ' + worker_data[name] )
                else:
                    print('Data Not Found..!!')
                    f_ask  = input('Do you want to exit enter:')
                    if f_ask.lower() == 'q':
                        exit()

        elif ask_find.lower() == 'client':

            for name in worker_data.keys():
                ask_find_name_c = input('Enter the name:')
                if name == ask_find_name_c.title():
                    print('Data Is Available ' + 'Name: ' + name.title() + ' Designation: ' + worker_data[name] )
                else:
                    print('Data Not Found..!!')
                    f_ask = input('Do you want to exit enter:')
                    if f_ask.lower() == 'q':
                        exit()
        else:
            print('Invalid Command..!!')

     def driver_function(self):
         pass_id = int(input('Enter the id:'))

         self.security_check_op(pass_id)

         ask_out = input('Please Specify The Type Of Data You Want(Worker,Client or Add):')

         if ask_out.lower() == 'worker':
             self.worker_database_outer_op()
             self.finding_data_under_op()

         elif ask_out.lower() == 'client':
             self.client_database_outer_op()
             self.finding_data_under_op()

         elif ask_out.lower() == 'add':
             self.adding_data_under_op()
             self.finding_data_under_op()

d1 = Company_Databse()
d1.driver_function()








