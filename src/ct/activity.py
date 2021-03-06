# -*- coding: utf-8 -*-
# Copyright 2011 Alf Lervåg. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#    1. Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#    2. Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials
#       provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY ALF LERVÅG ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL ALF LERVÅG OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and
# documentation are those of the authors and should not be interpreted
# as representing official policies, either expressed or implied, of
# Alf Lervåg.

import datetime
import decimal

class Activity(object):
    def __init__(self, date, project_id, duration, comment, salary_id="", read_only=False):
        if not isinstance(date, datetime.date):
            raise TypeError("date argument should be a date object")
        
        if not isinstance(duration, decimal.Decimal):
            raise TypeError("duration argument should be a decimal")

        self._dict = {
            'date': date,
            'project_id': project_id,
            'salary_id': salary_id,
            'duration': duration,
            'comment': comment,
            'read_only': read_only,
        }

    def __cmp__(self, other):
        return cmp(
            (self.date, self.project_id),
            (other.date, other.project_id))

    def __eq__(self, other):
        return self._dict == other._dict

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash((self.date, self.project_id))

    def __str__(self):
        return str(self._dict)

    @property
    def day(self):
        """DEPRECATED"""
        return self._dict['date']

    @property
    def date(self):
        return self._dict['date']

    @property
    def full_project_id(self):
        parts = tuple(self.project_id.split(","))
        return "projectid=%s,taskid=%s,subtaskid=%s,activityid=%s" % parts

    @property
    def project_id(self):
        return self._dict['project_id']

    @property
    def salary_id(self):
        return self._dict['salary_id']

    @property
    def duration(self):
        return self._dict['duration']

    @property
    def comment(self):
        return self._dict['comment']

    @property
    def is_read_only(self):
        return self._dict['read_only']

