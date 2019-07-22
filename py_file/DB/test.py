import pymysql

db = pymysql.connect(host='localhost', port=3307, user='root', passwd='021021', db='opentutorials')
cursor = db.cursor()

print(cursor)
#sql = "쿼리문"

#cursor.execute(sql)
print(cursor.execute("select * from 메이커"))

#db.commit()
