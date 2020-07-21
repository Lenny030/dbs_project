from configparser import ConfigParser


def read_db_config(filename='config.ini', section='mysql'):

    """reads databaseconfigfile and return a dictonary object
    :param filename: anem of the configfile
    :param section: section of database config
    :return: a dictonary of database parameters
    """
    #create parser and read ini configfile
    parser = ConfigParser()
    parser.read(filename)

    #get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)

        for item in items:
            db[item[0]] = item[1]

    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db

