students={
    '1':{
        'name' : 'Dung di',
        'grades':{
            'python':8,
            'web' :7,
            'English':10
        }
    },
      '2':{
        'name' : 'Dung diB',
        'grades':{
            'python':6,
            'web' :7,
            'English':8
               }
          },
        '3':{
        'name' : 'Dung diC',
        'grades':{
            'python':9,
            'web' :9,
            'English':10
        }  
}
}
for i in students:
    TB=0
    for grades in students[i]['grades']:
        TB +=students[i]['grades'][grades]
    TB = TB/len(students[i]['grades'])
    students[i]['TB']=TB
    #print(TB)
    #print({i})

for i in students:
    for grade in students[i]['grades']:
        print(f'{grade}: {students[i]["grades"]}')
    print(f'TB:{students[i]["TB"]}')
                                    
    
