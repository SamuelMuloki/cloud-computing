const express = require('express')
const mongoose = require('mongoose')
const filmRoute = require('./routes/films')
const app = express()

app.use(express.json())
mongoose.connect('mongodb://localhost:27017/films', { useNewUrlParser: true, useUnifiedTopology: true })

app.use('/films', filmRoute)

app.listen(3000, () => {
    console.log('Server is up and running...')
})