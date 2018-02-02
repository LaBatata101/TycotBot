from .models.base import Base, engine, Session
from .queries import make_query
from .models.group import Group


session = Session()


def commit():
    '''Commit the changes to database'''
    session.commit()


def close():
    '''Close the session connection with the database'''
    session.close()


def create_tables():
    '''
    see: 
      http://docs.sqlalchemy.org/en/latest/core/metadata.html#creating-and-dropping-database-tables
    '''
    Base.metadata.create_all(engine)


def addto_db(table):
    '''
    Get a table and add to db
    '''
    session.add(table)


def addsto_db(tables):
    '''
    Get a list of tables and add to db
    '''
    for table in tables:
        session.add(table)


def _current_session_obj(o):
    '''
    SqlAlchemy stuff
    see: https://stackoverflow.com/questions/24291933/sqlalchemy-object-already-attached-to-session
    '''
    curr_session = session.object_session(o)
    curr_session.add(o)
    curr_session.commit()
    curr_session.close()


def update_value(group_id, field, value):
    session.query(Group).filter(Group.group_id == group_id).update({field: value})


def set_welcome_msg(group_id, text):
    update_value(group_id, 'welcome_msg', text)
    commit_and_close()
    # group = make_query(Group, Group.group_id == group_id)[0]
    # group.welcome_msg = text
    # _current_session_obj(group)


def set_rules(group_id, text):
    update_value(group_id, 'rules', text)
    commit_and_close()
    # group = make_query(Group, Group.group_id == group_id)[0]
    # group.rules = text
    # _current_session_obj(group)


def set_chat_link(group_id, link):
    update_value(group_id, 'link', link)
    commit_and_close()


def commit_and_close():
    commit()
    close()
