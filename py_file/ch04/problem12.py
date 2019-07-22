#zip() 함수를 사용하여 다음 두 리스트를 짝으로 하는 movies 딕셔너리를 만들어라
titles = ['Creature of Habit','Crewel Fate']
plots = ['A nun turns into a monster','A haunted yarn shop']
movies = dict(zip(titles,plots))
print(movies)