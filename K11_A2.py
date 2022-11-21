tel = {
    'arbeit': {'Jan': '50', 'Mark': '81'},
    'private': {'Julia': '0151438924', 'Mark': '016932834'}
}

# 1. Ändere nachträglich die interne Durchwahl von Mark zu 80.
tel['arbeit']['Mark'] = '80'

# 2. Lösche den Eintrag von Julia inkl. Handynummer
del tel['private']['Julia']

# 3. Ändere den Namen Mark im privaten Bereich in „Murad“
tel['private']['Murad'] = tel['private'].pop('Mark')

print(tel)

