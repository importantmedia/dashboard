from django.db import connection

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def filldata_by_tag(tag_id):
    cursor = connection.cursor()
    sql = """SELECT tag_id, SUM(attempts) AS attempts, SUM(loads) AS loads, SUM(rejects) AS rejects
        FROM fills_minute WHERE tag_id = %s
        AND minute > DATE_SUB(NOW(), INTERVAL 1 HOUR)
        GROUP BY tag_id"""
    params = [ tag_id ]
    cursor.execute(sql, params)
    rows = dictfetchall(cursor)
    if len(rows) > 0:
        out = {
            'attempts': rows[0]['attempts'],
            'loads': rows[0]['loads'],
            'rejects': rows[0]['rejects'],
            'fill_rate': rows[0]['loads'] / rows[0]['attempts']
        }
    else:
        out = {
            'attempts': 0,
            'loads': 0,
            'rejects': 0,
            'fill_rate': 0
        }
    return out
