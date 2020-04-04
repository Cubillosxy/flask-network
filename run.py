import time
from blog import app
from blog import db


def database_initialization_sequence():
    from blog import User
    print('db init...')
    test_rec = User(
        username='edwinc',
        email='edwin@gmail.com',
        #'demo.jpg',
        password='demopass',
    )

    db.session.add(test_rec)
    db.session.rollback()
    print('db test complete. ')
    db.session.commit()


if __name__ == '__main__':
    dbstatus = False
    while dbstatus == False:
        try:
            db.create_all()
        except:
            time.sleep(2)
        else:
            dbstatus = True
    #database_initialization_sequence()
    app.run(debug=True, host='0.0.0.0')
