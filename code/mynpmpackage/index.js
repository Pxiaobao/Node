const date = require('./dateFormate')
const escape = require('./htmlEscape')

module.exports = {
    ...date,
    ...escape
}
