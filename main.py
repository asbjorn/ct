#!/usr/bin/env python

import sys
import cmd
from post import CurrentTime
from collections import defaultdict
from datetime import datetime

class CTCommands(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.ct = CurrentTime()

    def do_mywork(self, parms):
        print("**** Overview of your work ****")
        result = defaultdict(lambda: 0)
        for date, project, hours, comment in self.ct.get_hours():
            #print("date: %s, project: %s, hours: %s, comment: %s" % 
            #        (date, project, hours, comment)
            #        )
            result[project] += hours

        print("now projects....")
        self.projects = self.ct.get_projects()

        for project, worked in result.items():
            #print("project: %s, worked: %s" % (project, worked))
            print "%04s: %s" % (worked, self.projects[project].full_name)

    def do_EOF(self, parms):
        print("Quiting CurrenTime shell..")
        sys.exit()


if __name__ == '__main__':
    ct_cmd = CTCommands()
    ct_cmd.cmdloop()
