const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const routes = require('./routes');
require('dotenv').config();

const app = express();

app.use(express.json());
app.use(routes);

const mongoUser = process.env.USER_NAME
const mongoPass = process.env.USER_PASSWORD

mongoose.connect(`mongodb+srv://${mongoUser}:${mongoPass}@clusterapi.w58r7th.mongodb.net/api_db?retryWrites=true&w=majority&appName=clusterApi`).then(() => {
    app.listen(3000, () => {
        console.log('Conectado ao MongoDB');
        console.log('Server is running on port 3000');
    })
}).catch((err) => console.log(err));