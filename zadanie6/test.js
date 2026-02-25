const request = require('supertest')
const app = require('./app')
const service = require('./service')

beforeEach(() => {
  service.books = []
  service.readers = []
})

test('1. Добавление книги', async () => {
  const res = await request(app)
    .post('/books')
    .send({ title: 'Война и мир', author: 'Лев Толстой' })

  expect(res.status).toBe(200)
  expect(res.text).toBe('Книга добавлена')
  expect(service.allBooks().length).toBe(1)
  expect(service.allBooks()[0].title).toBe('Война и мир')
})

test('2. Удаление книги', async () => {
  service.addBook('Книга для удаления', 'Автор')
  const id = service.allBooks()[0].id

  const res = await request(app).delete(`/books/${id}`)

  expect(res.status).toBe(200)
  expect(res.text).toBe('Книга удалена')
  expect(service.allBooks().length).toBe(0)
})

test('3. Регистрация читателя', async () => {
  const res = await request(app).post('/readers').send({ name: 'Иван Иванов' })

  expect(res.status).toBe(200)
  expect(res.text).toBe('Читатель зарегистрирован')
  expect(service.readers.length).toBe(1)
  expect(service.readers[0].name).toBe('Иван Иванов')
})

test('4.Получение всех читателей', async () => {
  service.addReader('Иван Иванов')
  service.addReader('Петр Петров')

  const res = await request(app).get('/readers')

  expect(res.status).toBe(200)
  expect(Array.isArray(res.body)).toBe(true)
  expect(res.body.length).toBe(2)
  expect(res.body[0].name).toBe('Иван Иванов')
  expect(res.body[1].name).toBe('Петр Петров')
})

test('5. Выдача книги читателю ', async () => {
  service.addBook('Преступление и наказание', 'Ф. Достоевский')
  service.addReader('Петр Петров')

  const bookId = service.allBooks()[0].id
  const readerId = service.readers[0].id

  const res = await request(app).post('/borrow').send({ bookId, readerId })

  expect(res.status).toBe(200)
  expect(res.text).toBe('Книга выдана')
  expect(service.allBooks()[0].available).toBe(false)
})

test('6. Возврат книги Действия', async () => {
  service.addBook('Мастер и Маргарита', 'М. Булгаков')
  service.addReader('Сидор Сидоров')
  const bookId = service.allBooks()[0].id
  const readerId = service.readers[0].id

  service.borrowBook(bookId, readerId)

  const res = await request(app).post('/return').send({ bookId })

  expect(res.status).toBe(200)
  expect(res.text).toBe('Книга возвращена')
  expect(service.allBooks()[0].available).toBe(true)
})

test('7. Выдача уже занятой книги', async () => {
  service.addBook('Евгений Онегин', 'А. Пушкин')
  service.addReader('Алексей')
  service.addReader('Борис')

  const bookId = service.allBooks()[0].id
  const reader1Id = service.readers[0].id
  const reader2Id = service.readers[1].id

  await request(app).post('/borrow').send({ bookId, readerId: reader1Id })

  const res = await request(app)
    .post('/borrow')
    .send({ bookId, readerId: reader2Id })

  expect(res.status).toBe(400)
})

test('8. Возврат книги, которая не была взята', async () => {
  service.addBook('Обломов', 'И. Гончаров')
  const bookId = service.allBooks()[0].id

  const res = await request(app).post('/return').send({ bookId })

  expect(res.status).toBe(400)
})
