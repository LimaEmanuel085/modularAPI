const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();

app.listen(3000, () => {
    console.log('Server is running on port 3000');
})