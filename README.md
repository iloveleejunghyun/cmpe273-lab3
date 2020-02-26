# ariadne_graphql_prac  
graphql + adridne + sqlite3 + alchemy + jwt  

to be done:
    delete student, class by id. concurrently delete map.

client:  
---------------- student  
{  
	student(id:1){  
	    id  
	    name   
	}  
}  
{  
	students{    
	    id   
	    name   
	}  
}  
mutation {  
	createStudent(name:"Vatsa1"){  
	    id  
	    name   
	}  
}  

---------------- class  
{  
	class(id:1){  
	    id  
	    name  
		students{  
			id  
			name  
		}  
	}  
}  
{  
	classes{  
	    id  
	    name  
		students{  
			id  
			name  
		}  
	}  
}  
mutation {  
	createClass(name:"CMPE273"){  
	    id  
	    name  
	}  
}  
---------------class students map  
mutation {  
	addStudentToClass(classId:1, studentId:1){  
	    id  
	    name  
		students{  
			id  
			name  
		}  
	}  
}  

