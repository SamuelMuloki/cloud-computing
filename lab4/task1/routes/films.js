const express = require('express')
const router = express.Router()

const Film = require('../models/Film')
const verifyToken = require('../verifyToken')

router.get('/', verifyToken, async (req, res) => {
    try {
        const films = await Film.find()
        res.send(films)
    } catch (err) {
        res.status(400).send({ message: err })
    }
})

router.post('/', verifyToken, async (req, res) => {
    const filmData = new Film({
        film_name: req.body.film_name,
        film_type: req.body.film_type,
        film_year: req.body.film_year,
        film_link: req.body.film_link
    })

    try {
        const savedFilm = await filmData.save()
        res.send(savedFilm)
    } catch (err) {
        res.status(400).send({ message: err })
    }
})

module.exports = router