exports.books = []
exports.readers = []

exports.allBooks = () => exports.books

exports.allReaders = () => exports.readers

exports.addBook = (title, author) => {
  exports.books.push({
    id: Math.random().toString(36).substr(2, 9),
    title,
    author,
    available: true,
  })
}

exports.removeBook = (id) => {
  const index = exports.books.findIndex((b) => b.id === id)
  if (index !== -1) exports.books.splice(index, 1)
}

exports.addReader = (name) => {
  exports.readers.push({
    id: Math.random().toString(36).substr(2, 9),
    name,
  })
}

exports.borrowBook = (bookId, readerId) => {
  const book = exports.books.find((b) => b.id === bookId && b.available)
  const reader = exports.readers.find((r) => r.id === readerId)
  if (book && reader) {
    book.available = false
    return true
  }
  return false
}

exports.returnBook = (bookId) => {
  const book = exports.books.find((b) => b.id === bookId && !b.available)
  if (book) {
    book.available = true
    return true
  }
  return false
}
