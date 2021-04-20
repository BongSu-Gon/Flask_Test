import pymysql #pymysql 라이브러리 가져옴
db = pymysql.connect( #접속환경 설정; 키값 설정 후, 새로운 인스턴스(db) 생성
    host='localhost',
    port = 3306,
    user = 'root',
    password = '1234',
    db = 'busan'
)
###쿼리문 날리기
sql = '''
CREATE TABLE `topic` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `title` varchar(100) NOT NULL,
    `body` text NOT NULL,
    `author` varchar(30) NOT NULL,
    `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
    ) ENGINE=innoDB DEFAULT CHARSET=utf8;
'''
sql_1 = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES ('부산', '부산와서 갈매기를 못봤네', '신동찬');"
sql_2 = "INSERT INTO `busan`.`users` (`name`, `email`, `username`, `password`) VALUES ('동찬', '1220zpqls@gmail.com', 'SHIN', '12345');"
sql_3 = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
# title = input('제목을 적으세요')
# body = input('내용을 적으세요')
# author = input('누구세요?')
input_data = [title, body, author]
cursor = db.cursor() #쿼리문을 실행시킬수 있는 메소드(cursor)
# db.cursor.@@ 매번 이렇게 쓸수 없으니 cursor에 할당
# cursor.execute(sql_1)
# cursor.execute(sql_2)
# cursor.execute(sql_3,input_data)
# db.commit() 
# # #sql apply버튼
# db.close() 
# #commit 중지
# cursor.execute(sql_1)
# cursor.execute(sql_2)
### 쿼리보내기 & 조회하기
# cursor.execute('SELECT * FROM busan.users;') #excute 안의 위치로 쿼리날리기
cursor.execute('SELECT * FROM topic;')
users = cursor.fetchall() #패치올메소드로 조회 & return
print(cursor.rowcount, users)