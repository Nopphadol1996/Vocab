import sqlite3
conn = sqlite3.connect('vocab.sqlite3')
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS vocabulary (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    tsid TEXT,
                    vocab TEXT,
                    Parts_of_Speech Text,   
                    translate TEXT,
                    sentence Text) """)

def insert_vocab(tsid,vocab,partofspeech,translate,sentence):
    #CREATE
    with conn:
        command = 'INSERT INTO vocabulary VALUES (?,?,?,?,?,?)'
        c.execute(command,(None,tsid,vocab,partofspeech,translate,sentence))
    conn.commit()
    #print('saved')


def view_vocab():
    # READ
    with conn:
        command = 'SELECT * FROM vocabulary'
        c.execute(command)
        result = c.fetchall()
    #print(result)
    return result

def update_vocab(tsid,field,newvalue):
    # UPDATE
    with conn:
        command = 'UPDATE vocabulary SET {} = (?) WHERE tsid=(?)'.format(field)
        c.execute(command,(newvalue,tsid))
    conn.commit()
    #print('updated')


def delete_vocab(tsid):
    # DELETE
    with conn:
        command = 'DELETE FROM vocabulary WHERE tsid=(?)'
        c.execute(command,([tsid]))
    conn.commit()
    #print('deleted')