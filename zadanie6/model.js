function createBook(title, author) {
  return {
    id: Math.random().toString(36).substr(2, 9),
    title,
    author,
    available: true,
  }
}

function createReader(name) {
  return {
    id: Math.random().toString(36).substr(2, 9),
    name,
  }
}

module.exports = { createBook, createReader }
