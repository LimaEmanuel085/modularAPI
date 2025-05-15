const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');

require('dotenv').config();

const app = express();

app.listen(3000, () => {
    console.log('Servidor iniciado na porta 3000');
    console.log('Acesse http://localhost:3000');
})