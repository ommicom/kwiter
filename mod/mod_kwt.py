__author__ = 'ommicom'

import os
import sqlite3
import datetime

sett = __import__('set_kwt')

def db_reestr(inf_row):
    db_name = sett.db.get('name', os.path.join(os.getcwd(),'kwt.sqlite'))
    con = sqlite3.connect(db_name, check_same_thread=False)
    try:
        cur = con.cursor()
        # for row in inf_row:
        #     cur.execute('INSERT INTO reestr (kwt, mes, kwt_res, kwt_dt, kwt_tm) VALUES (?, ?, ?, ?, ?)', row)
        #     cur.execute()
        cur.executemany('INSERT INTO reestr (kwt, mes, kwt_res, kwt_dt, kwt_tm) VALUES (?, ?, ?, ?, ?)', inf_row)
        con.commit()
    except sqlite3.OperationalError as err:
        print(err)
    finally:
        con.close()
    # print(inf_row)

    # con = sqlite3.connect(db_name, check_same_thread=False)
    # try:
    #     cur = con.cursor()
    #     cur.execute('INSERT INTO reestr(kwt, result, kwt_dt, kwt_tm) VALUES(?, ?, ?, ?)', (inf_row[0].replace('\n',''), inf_row[1].replace('\n',''), inf_row[2].replace('\n',''), inf_row[3].replace('\n','')))
    #     con.commit()
    # except sqlite3.OperationalError:
    #     con.execute('CREATE TABLE "main"."reestr" ("id_kwt" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL, "kwt" CHAR NOT NULL, "result" CHAR NOT NULL, "kwt_dt" CHAR NOT NULL,'
    #                 '"kwt_tm" CHARE NOT NULL, "dt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP)')
    # con.close()

def run(files, mod_result=None):
    try:
        reestr_dir = sett.reestr_dir
    except AttributeError:
        reestr_dir = os.getcwd()
    try:
        post_dir = sett.post_dir
    except AttributeError:
        post_dir = os.getcwd()

    db_enable = sett.db.get('mode', False)
    res_row = list()
    for kwt in files:
        with open(kwt, 'r', encoding='cp866') as f:
            inf_row = list()
            context_ = f.read()
            part_ = context_.split('###')
            subpart = list(map((lambda x: x.replace('\n', '')), part_[1].split('@@@')))
            inf_row.append(os.path.basename(kwt))
            inf_row.append(part_[0])
            inf_row.append(subpart[0])
            inf_row.append(subpart[1])
            inf_row.append(subpart[2])
        res_row.append(inf_row)
        os.rename(kwt, ''.join((post_dir, '~'.join(('',os.path.basename(kwt))))))

    if res_row:
        dt = 'reestr_'+datetime.datetime.today().strftime('%Y%m%d%H%M%S')+'.txt'
        with open(os.path.join(reestr_dir, dt), 'w') as f:
            for res in res_row:
                f.write('\t'.join(res))
                f.write('\n')
        if db_enable:
            db_reestr(res_row)

    return files, mod_result