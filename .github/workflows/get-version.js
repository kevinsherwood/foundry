let fs = require('fs')
console.log("v",JSON.parse(fs.readFileSync('./module.json', 'utf8')).version)