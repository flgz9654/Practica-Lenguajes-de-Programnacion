// Encontrar el numero mayor de una lista de numeros en un array

let num = [5, 10, 15, 60, 8]
let numMax = 0
let size = num.length

for (let i = 0; i < size; i++) {
  if (numMax < num[i]) {
    numMax = num[i]
  }
}

console.log(numMax)

let max = Math.max(5, 10, 15, 60, 8)

console.log(max)