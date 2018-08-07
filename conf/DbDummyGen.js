db.auth({
    'user': 'root',
    'pwd': 'root'
});
db = db.getSiblingDB('viewgrade')

db['users'].deleteMany({
    'username': {
        $ne: 'admin'
    }
});

db['years'].deleteMany({});
db['semesters'].deleteMany({});
db['classes'].deleteMany({});

years = db['years'].insertMany([
    {
        'startYear': 2016
    },
    {
        'startYear': 2017
    },
]);

semesters = db['semesters'].insertMany([
    {
        'yearId': years['insertedIds'][0],
        'name': 'HK 1',
        'startDate': '2016-09-01',
    },
    {
        'yearId': years['insertedIds'][1],
        'name': 'HK 2',
        'startDate': '2018-02-01',
    },
]);

classes = db['classes'].insertMany([
    {
        'name': 'mon hoc 1',
        'code': 'SUB001',
        'scorePdfLink': null,
        'semesterId': semesters['insertedIds'][0],
    },
    {
        'name': 'mon hoc 2',
        'code': 'SUB002',
        'scorePdfLink': null,
        'semesterId': semesters['insertedIds'][0],
    },
    {
        'name': 'mon hoc 3',
        'code': 'SUB003',
        'scorePdfLink': null,
        'semesterId': semesters['insertedIds'][1],
    },
    {
        'name': 'mon hoc 4',
        'code': 'SUB004',
        'scorePdfLink': null,
        'semesterId': semesters['insertedIds'][1],
    },
]);
