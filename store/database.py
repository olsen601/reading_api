import os
import psycopg2


DATABASE = os.environ['DATABASE']
USER = os.environ['USER']
PASSWORD = os.environ['RL_DB_PW']
HOST = os.environ['HOST']
PORT = '5432'
# based on psycopg2 doc structure of connection


conn = psycopg2.connect(dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
cur = conn.cursor()


def insert_data(items_data):

    insert_author = '''
        INSERT INTO reading_author (name)
        VALUES (%s)
        ON CONFLICT DO NOTHING;
    '''
    #RETURNING id doesn't work, needs more research documentation is lite
    # have to use %s, won't take ? instead and docs use them

    insert_categorie = '''
        INSERT INTO reading_categorie (name)
        VALUES (%s)
        ON CONFLICT DO NOTHING;
    '''

    insert_book = '''
        INSERT INTO reading_book (google_id, self_link, title, publisher, published_date, description, isbn_13, isbn_10, small_thumbnail, author_id)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,
        (SELECT id FROM reading_author WHERE name=%s))
        ON CONFLICT DO NOTHING;
    '''


    with conn:
        try:
            for item in range(0,(len(items_data))):
                data = items_data['item_'+(str(item))]
                author = data['author'][0]
                categorie = data['categorie']

                google_id = data['google_id']
                self_link = data['self_link']
                title = data['title']
                try:
                    publisher = data['publisher']
                except:
                    publisher = "No Publisher"
                    pass
                published_date = data['published_date']
                description = data['description']
                isbn_13 = data['isbn_13']
                isbn_10 = data['isbn_10']
                small_thumbnail = data['small_thumbnail']

                cur.execute(insert_author, (author,))
                #returning originally used the above statement to set author_id
                cur.execute(insert_categorie, (categorie,))
                cur.execute(insert_book, (google_id, self_link, title, publisher, published_date, description, isbn_13, isbn_10, small_thumbnail, author))
                conn.commit()

                p = print('uploaded data')
            return p

        except psycopg2.Error as e:
            print(e.pgerror)
            # should print readable error message
            pass
