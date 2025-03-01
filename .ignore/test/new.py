import numpy

AP = {'AP1': {'start': 1027.17, 'stop': 1041.0}, 'AP2': {'start': 1041.0, 'stop': 1056.0},
      'AP3': {'start': 1056.0, 'stop': 1072.0}, 'AP4': {'start': 1072.0, 'stop': 1089.0},
      'AP5': {'start': 1089.0, 'stop': 1106.0}, 'AP6': {'start': 1106.0, 'stop': 1124.0},
      'AP7': {'start': 1124.0, 'stop': 1144.0},
      'AP8': {'start': 1144.0, 'stop': 1163.0}, 'AP9': {'start': 1163.0, 'stop': 1180.0},
      'AP10': {'start': 1180.0, 'stop': 1200.0}, 'AP11': {'start': 1200.0, 'stop': 1220.0},
      'AP12': {'start': 1220.0, 'stop': 1238.0}, 'AP13': {'start': 1259.0, 'stop': 1279.0},
      'AP14': {'start': 1279.0, 'stop': 1298.0}, 'AP15': {'start': 1298.0, 'stop': 1319.0},
      'AP16': {'start': 1319.0, 'stop': 1339.0}, 'AP17': {'start': 1339.0, 'stop': 1360.0},
      'AP18': {'start': 1383.0, 'stop': 1404.0}, 'AP19': {'start': 1404.0, 'stop': 1428.0},
      'AP20': {'start': 1428.0, 'stop': 1450.0}, 'AP21': {'start': 1450.0, 'stop': 1473.0},
      'AP22': {'start': 1473.0, 'stop': 1495.0}, 'AP23': {'start': 1495.0, 'stop': 1520.0},
      'AP24': {'start': 1545.0, 'stop': 1573.0}, 'AP25': {'start': 1573.0, 'stop': 1598.0},
      'AP26': {'start': 1598.0, 'stop': 1626.0},
      'AP27': {'start': 1626.0, 'stop': 1652.0}, 'AP28': {'start': 1652.0, 'stop': 1677.0},
      'AP29': {'start': 1677.0, 'stop': 1703.0}, 'AP30': {'start': 1703.0, 'stop': 1731.0},
      'AP31': {'start': 1731.0, 'stop': 1757.0}, 'AP32': {'start': 1989.3, 'stop': 2020.6},
      'AP33': {'start': 1786.0, 'stop': 1817.0}, 'AP34': {'start': 1817.0, 'stop': 1843.0},
      'AP35': {'start': 1843.0, 'stop': 1870.0}, 'AP36': {'start': 1870.0, 'stop': 1900.0},
      'AP37': {'start': 1900.0, 'stop': 1931.0}, 'AP38': {'start': 1931.0, 'stop': 1961.0},
      'AP39': {'start': 1961.0, 'stop': 1989.0}, 'AP40': {'start': 1361.2, 'stop': 1383.5},
      'AP41': {'start': 1238.0, 'stop': 1259.0}, 'AP42': {'start': 1520.1, 'stop': 1545.42},
      'AP43': {'start': 1758, 'stop': 1786.5}}
a = []
for i in AP:
    a.append(AP[i]['start'])
print(numpy.sort(a))
print(len(a))
