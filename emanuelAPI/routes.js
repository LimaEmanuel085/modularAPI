const express = require('express');
const route = express.Router();

const userController = require('./controllers/userController');

route.get('/', userController.viewUser);
route.post('/create', userController.createUser);

module.exports = route;