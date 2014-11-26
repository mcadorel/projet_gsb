#-*-coding: utf-8
# mael.cadorel@laposte.net

""" Test connexion SQL server avec pymssql. """

import pymssql


class Model(object):
    """ Connexion à la base de données de GSB_RV sur SQL Server. """
    def __init__(self, _host, _database, _user, _password):
        try:
            self.connectGsb = pymssql.connect(
                    host=_host,
                    database=_database,
                    user=_user,
                    password=_password
                    )
            self.cursor = self.connectGsb.cursor()
        except pymssql.OperationalError:
            print('Echec de la connexion à la base de données.')
            exit(0)

    def query(self, query:'SQL string'):
        """ Renvoie une liste de tuples. """
        self.cursor.execute(query)
        return self.cursor.fetchall()

# test
if __name__ == '__main__':
    m = Model(input('Host ?'),
              input('Database'),
              input('User ?'),
              input('Password ?'))
    clefs   = m.query('SELECT idFamille FROM FAMILLE')
    valeurs = m.query('SELECT libFamille FROM FAMILLE')

    print('DEBUG : \n' + '\n'.join(str(val)[2:-3] for val in valeurs))
