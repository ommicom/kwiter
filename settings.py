log_settings = {'name':'kwiter', 'level':'debug', 'out':'con'}
smtp_settings = {}#?
db_settings = {}
scan_settings = [{'scan_dir':('',), 'mask':('',), 'actor':('mod_sqlite', 'mod_arch')},
                 {'scan_dir':('',), 'mask':('',), 'actor':'mod_smtp'},
                 {'scan_dir':('',), 'mask':('',), 'actor':'mod_arch'}
                ]
cycle = 10