const express = require('express')
const app = express()
const {
  allBooks,
  allReaders,
  addBook,
  removeBook,
  addReader,
  borrowBook,
  returnBook,
} = require('./service')

app.use(express.json())

app.get('/books', (req, res) => res.json(allBooks()))

app.post('/books/create', (req, res) => {
  addBook(req.body.title, req.body.author)
  res.send('Книга добавлена')
})

app.delete('/books/delete/:id', (req, res) => {
  removeBook(req.params.id)
  res.send('Книга удалена')
})

app.get('/readers', (req, res) => res.json(allReaders()))

app.post('/readers/register', (req, res) => {
  addReader(req.body.name)
  res.send('Читатель зарегистрирован')
})

app.post('/borrow', (req, res) => {
  if (borrowBook(req.body.bookId, req.body.readerId)) {
    res.send('Книга выдана')
  } else {
    res.status(400).send('Невозможно выдать книгу')
  }
})
app.post('/return', (req, res) => {
  if (returnBook(req.body.bookId)) {
    res.send('Книга возвращена')
  } else {
    res.status(400).send('Невозможно вернуть книгу')
  }
})

const PORT = 3000
app.listen(PORT, () => console.log(`Сервер запущен на порту ${PORT}`))

module.exports = app
