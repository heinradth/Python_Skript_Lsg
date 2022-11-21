tel = {
    'arbeit': {'Jan': '50', 'Mark': '81'},
    'private': {'Julia': '0151438924', 'Mark': '016932834'}
}

print(len(tel))
print(len(tel['arbeit']))
print(tel['arbeit'].get('Mark'))
print('Jan' in tel['arbeit'])
print(list(tel['private'].values()))
print(tel['private'].copy())
