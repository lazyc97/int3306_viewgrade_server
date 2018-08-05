db.auth({
    user: 'root',
    pwd: 'root',
})

db = db.getSiblingDB('viewgrade')

db.createCollection('users');
db.createCollection('years');
db.createCollection('semesters');
db.createCollection('classes');

db['users'].createIndex({
    'username': 1,
}, {
    unique: true,
});

db['years'].createIndex({
    'startYear': -1,
}, {
    unique: true,
});

db['semesters'].createIndex({
    'yearId': 1,
});

db['classes'].createIndex({
    'semesterId': 1,
});
