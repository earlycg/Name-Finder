1	names = ["Ana", "Bruno", "Clara", "Diego", "Elena", "Federico", "Gabriela", "Hugo", "Inés", "Javier", "Karen", "Leonardo", "Mariana", "Nicolás", "Olivia", "Pablo", "Quirino", "Rosa", "Santiago", "Tatiana", "Ulises", "Valentina", "Wendy", "Xavier", "Yolanda", "Zacarías", "Ariel", "Bárbara", "Camilo", "Daniela", "Emiliano", "Florencia", "Gerardo", "Helena", "Ignacio", "Julieta", "Kevin", "Lucía", "Mateo", "Natalia", "Octavio", "Patricia", "Quimera", "Ricardo", "Soledad", "Tomás", "Uxía", "Valentín", "Ximena", "Yahir", "Zenaida", "Andrés", "Beatriz", "Carlos", "Delfina", "Esteban", "Fabiola", "Gonzalo", "Hilda", "Iván", "Benjamín", "Carolina", "Daniel", "Francisco", "Héctor", "Isabel", "Jorge", "Luis", "María", "Pedro", "Quetzal", "Raquel", "Teresa", "Uriel"]
2	
3	capital_letters = input("Enter the first letter or letters of the name you are looking for: \n ->").capitalize()
4	i = len(capital_letters)
5	filtered_names = list(filter(lambda name: name[0:i] == capital_letters, names))
6	
7	print(filtered_names)
