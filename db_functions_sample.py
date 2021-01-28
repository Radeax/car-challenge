import mysql.connector
from connection import getConnection


def addPerson(fname, lname):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO people (fname, lname) VALUES ('{fname}', '{lname}')")
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()


def removePerson(id):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"DELETE FROM people WHERE person_id={id}")
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()


def updateFirstName(id, fname):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE people SET fname = '{fname}' WHERE person_id={id}")
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()


def updateLastName(id, lname):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE people SET lname = '{lname}' WHERE person_id={id}")
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()


def selectAll():
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM people")
        result = cursor.fetchall()
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        cursor.close()

    return result


def printAll():
    for person in selectAll():
        print(person)

# addPerson('John', 'Wick')
# removePerson(2)
# updateFirstName(3, "HI")


print(printAll())
# print(selectAll())
